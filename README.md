# MyStocks

## Business Domain

### Core Domain
This project serves as backend for monitoring personal stocks. In order to do so
it requests information from the API of yahoo available at    

https://rapidapi.com/apidojo/api/yh-finance/

The response is then processed such that relevant information is retrieved and
returned to the frontend app. Note that in order not to invoke the external API on each
request we save the data in a local database which acts as a cache for subsequent invocations.
Thus, we only synchronize with yh-finance API in the following cases:  
  - New stocks shall be monitored
  - Information for a given stock has not been updated for some time (e.g. 3 days for ratings, once a year for value computation and financial data from yearly reports)

The general concept is illustrated in the following runtime view (note that a similar flow of data applies to the computation of a companies value):    

![img.png](docs/runtime-view.png)

More information concerning the core domain of our app as well as technical aspects of the api we consume can
be found in the docs folder (in particular in finanzen.md and yh-finance.txt)
    
### Usecases
Next to the core usecase described in the previous chapter, the following features are provided:  
- administrative task: map displayed stock names to API params (CRUD /mapping)
- administrative task: show api invocation count
- administrative task: provide possibility to upload csv of mappings
- administrative task: database import and export
- choose which of the stocks (registered in mappings) should be shown and requested (/stocks)
- computation of a companies values (requires invocation of yh-finances to retrieve free cash flows)
- retrieval of financial data from annual report
- frontend: highlight underrated stocks
- frontend: exclamation mark on stock when quarterlies are close or rating has changed
    
### External API
We request yh-finance to receive up-to-date information regarding our stocks of interest. Since we stick
to the free plan, we can only fire 500 request a month against said API. We thus only call yh-finance
if the information for a given entry in the database has not been updated in the last three days (for statistics) / in the last year (for financial data). 
Still, once many stocks are shown in our app, we might still hit 500 API calls in a given month. For that purpose
we count the number of calls per month and stop hitting the API once we are close to 500.

### Database Schema
The table below illustrates the schema of our stocks database:  

LookUps                | ApiCounter                            | Aktie                                   |
---------------------- | ------------------------------------- | --------------------------------------- |
id (int)               | id (int)                              | id (int)                                |
app_name (string)      | anfangsdatum_30_tage_periode (date)   | lookup_id (int)                         |
api_name (string)      | count (int)                           | datum_naechster_quarterly_report (date) |
|                      |                                       | aktueller_preis (double)                | 
|                      |                                       | aktiv (boolean)                         | 

Bewertung                                  | Fundamentalanalyse                     |  
------------------------------------------ | -------------------------------------- |
id (int)                                   | id (int)                               |
aktie_id (int)                             | aktie_id (int)                         | 
kgv (double)                               | fcfs (string)                          |
kbv (double)                               | datum_guv (date)                       |
anzahl_bewertungen (int)                   | ebit (double)                          | 
durchschnittliche_bewertung (double)       | jahresumsatz (double)                  | 
minimaler_preise (double)                  | datum_bilanz (date)                    |
maximaler_preis (double)                   | eigenkapital (double)                  | 
durchschnittlicher_preis (double)          | gesamtvermoegen (double)               |
datum_letzter_stats_api_aufruf (double)    | datum_letzter_guv_api_aufruf (date)    |
|                                          | datum_letzter_guv_bilanz_aufruf (date) |

## Local Setup

### Setting up dependencies
Create a virtual environment either via command line or if using IntelliJ in terms of a new project SDK
and configure to use it in Project Structure. Using IntelliJ you can now open requirements.txt and simply
follow the suggestion to install the specified dependencies. As the new virtual environment ist configured 
as project SDK, the corresponding packages will be automatically installed in the right location within the virtual
environment, i.e. site-packages. Otherwise, using command line you need to activate the virtual environment explicitly
and then install the dependencies via pip thereby passing the requirements.txt file as a parameter to the 
pip install command.

### Running the project
In order to run the project locally, you need to install docker and start the postgres database
from the root directory of the project using ```docker-compose up```    
Further, there are two profiles - dev and local - to run the application (note that the former uses mock
data instead of actually requesting information from yh-finance). They are configured in terms of config.py.
The profiles can be activated by configuring corresponding runners. The configuration for e.g. the dev profile
in IntelliJ looks as follows:
![img.png](docs/run-config.png)

