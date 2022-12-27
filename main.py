"""A ideia geral é usar várias API's para pesquisar os preços de voos para diversas cidades da data atual
 até seis meses para frente, depois lançar esse valor em um planilha no GOOGLE DOCS e então mandar um SMS
  quando tiver uma promoção com valor mais baixo."""
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"
"""esse if é para caso a coluna iata code esteja vazia ele roda o código e já preenche"""
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
"""a biblioteca datetime lida com datas e timedelta calcula a diferença de duas datas"""
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
"""esse for loop vai passar por todas os destinos na coluna iataCode do GoogleSheet, para depois o 
if achar o menor preço e mandar o sms. Reparar que o check_flights é uma função e aqui, pelo que entendi,
foram passados somente os atributos necessários da função """
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
