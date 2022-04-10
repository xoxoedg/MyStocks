# MyStocks

This project serves as backend for monitoring personal stocks. In order to do so
it requests information from the API of yahoo available at    

https://rapidapi.com/apidojo/api/yh-finance/

The response is then processed such that relevant information is retrieved and
returned to the frontend app. Note that in order not to invoke the external API on each
request we save the data in a local database which acts as a cache for subsequent invocations.
Thus, we only synchronize with yh-finance API in the following cases:  
  - New stocks shall be monitored
  - Special events occured, for example quarterly reports have been submitted and the date of the next quarterlies must be inferred etc.

The general concept is illustrated in the following runtime view:
![img.png](docs/runtime-view.png)