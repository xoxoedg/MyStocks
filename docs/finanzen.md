# Finanzen

Diese Dokument beschreibt einige grundlegende Konzepte und zugehörige Vokabeln aus dem Bereich Finanzen
im Kontext dieser Applikation.

### Ziele der App

Der Kern der Applikation besteht darin, Informationen zur Bewertung von verschiedenen Wertpapieren und perspektivisch
alternativen Finanzkontrakten aggregiert zur Verfügung zu stellen. Der Fokus ist dabei die Fundamentalanalyse, die anhand
von Unternehmenskennzahlen (werden in Quartalsberichten durch die verschiedenen Unternehmen zur Verfügung gestellt) vorhersagt,
wie wertvoll ein Unternehmen ist. Mit einer solchen Analyse, weiteren Kennzahlen und Ratings von Analysten soll es möglich sein
Kaufentscheidungen zu vereinfachen und auf Basis eines soliden theoretischen Fundaments zu begründen.

### Grundlegende Vokabeln

Um die Fundamentalanalyse in ihren Grundlagen zu verstehen, benötigen wir einige Vokabeln (die zudem einen Teil der ```ubiquituous 
language``` der Fachdomäne dieses App widerspiegeln). Wenn nicht explizit anders spezifiziert beschreiben die Kennzahlen im Rahmen der 
App immer Wert bzgl. eines Jahres.

Bezeichnung in der App | Deutscher Begriff        | Englischer Begriff              | Bedeutung
---------------------- | ------------------------ | ------------------------------- | ---------
KGV                    | Kurs-Gewinn-Verhältnis   | Price-per-Earnings Ration (PER) | Kurs einer Aktie im Vergleich zum Gewinn; KGV < 15 indikativ für Value Unternehmen
KBV                    | Kurs-Buchwert-Verhältnis | Price-per-Booking Ration (PBR)  | Kurs einer Aktie im Vergleich zum Eigenkapital einer Aktie (Value entspricht KBV < 1)
Eigenkapital           | Eigenkapital             | Equity                          | Summe aus Kapital durch verkaufte Aktien + Sachwerte des Unternehmens (Assets) + anderweitiges nicht auf Verschuldung basierendes Kapital
Fremdkapital           | Fremdkapital             | Debts                           | Schulden aus Krediten und herausgegebenen Unternehmensanleihen
Free Cash Flow         | Freier Cash Flow         | Free Cash Flow                  | Purer Gewinn eines Unternehmens in einem Jahr - Reinvestitionen in Sachwerte; entspricht dem puren Wert der in einem Jahr erwirtschaftet wurde und im Prinzip an die Aktionäre ausgeschüttet werden kann
Eigenkapitalquote      | Eigenkapitalquote        | -                               | Eigenkapital geteilt durch Gesamtvermögen (Teil des Vermögens, der nicht über Schulden abgebildet wird)
Eigenkapitalrendite    | Eigenkapitalrendite      | Return on Equity                | Nettogewinn geteilt durch Eigenkapital
Aktien im Umlauf       | Aktien im Umlauf         | Shares Outstanding              | Aktien, die von Aktioären gehalten werden (also Aktien, die aktuell an Aktionäre verkauft sind)

Für die Implementierung unserer Applikation sind vorerst nicht alle der oben beschriebenen Konzepte relevant. Allerdings sind die genannten Kennzahlen für 
weiterführende Analysen sehr hilfreich. Zeigt unsere Anwendung zum Beispiel, dass es sich um eine unterbewertete Aktie handelt, die auch von Analysten empfohlen wird,
so lohnt es sich vor einem Kauf dennoch zusätzlich einige Unternehmensinformationen zusätzlich explizit zu checken. Dazu gibt es diverse Internetseiten,
die teilweise direkt oben genannte Infos, oder aber verwandte Kennzahlen bereitstellen, aus denen sich obige Werte berechnen lassen.
Hier ist eine kurze Liste mit Links, die als Einstieg helfen können (am Beispiel von Apple):    
- https://finance.yahoo.com/quote/AAPL/cash-flow?p=AAPL
- https://www.finanzen.net/bilanz_guv/apple
- https://www.ariva.de/apple-aktie/bilanz-guv
- https://www.onvista.de/aktien/fundamental/Apple-Aktie-US0378331005
- https://www.boerse-online.de/bilanz_guv/apple