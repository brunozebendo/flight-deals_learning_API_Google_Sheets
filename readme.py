"""esse projeto é muito grande, vou copiar as orientações no readme. Mas a ideia geral é usar várias
API's para pesquisar os preços de voos para diversas cidades da data atual até seis meses para frente,
depois lançar esse valor em um planilha no GOOGLE DOCS e então mandar um SMS quando tiver uma promoção com
valor mais baixo."""
"""Program Requirements
Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International
Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple
airports, you want the city code (not the airport code see here).
Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for
all the cities in the Google Sheet.
If the price is lower than the lowest price listed in the Google Sheet then send an SMS
to your own number with the Twilio API.
The SMS should include the departure airport IATA code, destination
airport IATA code, departure city, destination city, flight price and flight dates. e.g.
Toggle these options when setting up with the API providers
Sheety API
Avoid making too many unnecessary requests with the Sheety API while testing your code.
The free trier for the Sheety API only allows 200 requests per month.
Also, enable the PUT option so that you can write to your Google sheet
Register with the Kiwi Partners Flight Search API
Your account name should be the same as what you used later in "First name" and "Last name".
There is no need to provide a credit card or billing information (you can skip that section)
when you create your "Solution" (previously called "Application").
When registering for your API key choose Meta Search as your product type.
Then choose One-Way and Return.
In summary, your "solution" should look something like this:
If the website prompts you for the type of partnership you can either choose
"Book with Kiwi.com" or the affiliate program. Both should work for this project.

No primeiro passo é preciso criar um google sheets que vai servir para armazenar os dados dos preços e das
cidades, servindo como uma espécie de banco de dados, o segundo passo é testar a comunicação entre a API
sheety e o google docs através da função put. Depois é preciso incluir o IATA no Google DOCS (An IATA airport code,
 also known as an IATA location identifier, IATA station code, or simply a location identifier,
  is a three-character alphanumeric geocode designating many airports and metropolitan areas around
  the world, defined by the International Air Transport Association (IATA).)
  
  Analisando puramente o código, interpreto aqui os fundamentos do POO, já que foram aqui criadas cinco pastas,
  cada uma lidando com uma questão diferente, a main com o comando do código, outra armazenando os dados, 
  outra lidando com os dados, outra criando funções para a notificação e a última lidando com a busca por voos
"""