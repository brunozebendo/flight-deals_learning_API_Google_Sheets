import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = YOUR FLIGHT SEARCH API KEY

"""Essa pasta lida com o request do site Tequila que é parceiro do site Kiwi, pelo que entendi o 
KIWI vende passagens e para conseguir todas as informações para o negócio eles criaram o Tequila
e o disponibilizaram gratuitamente como API, para isso acima foi importada a biblioteca requests
e depois a classe FlighData da pasta flight_data, nessa
classe estão todas as informações do voo, como preço, cidade de origem, destino...Então foram
passadas duas variáveis constante que são o endpoint (endereço da API) e a chave KEY obrigatória.
Então foi criada uma nova classe que vai lidar com a busca pelos voos, para isso foi criada a função
get_destination_code, que, segundo os parâmetros estabelecidos na documentação do TEQUILA, e o padrão
de API é passado no query a informação q se quer e no final o return retorna o código IATA da cidade"""
class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
"""essa função vai checar os voos, para isso são passados os parâmetros abaixo, (reparar que foi
preciso primeiro achar o código da cidade por isso a função acima), no headers fica a KEY, obrigatória,
e no query todos os dados que se quer obter. Esse código é gerado no tequila."""
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
"""aqui a variavel response que vai efetivamente fazer o request das informações"""
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )
"""aqui a função do try para lidar com erro caso o voo não seja encontrado"""
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
"""pelo q entendi, essa parte é para armazenar os dados obtidos como um json. Reparar que aqui os
[] indicam qual parte do dicionário será usada. A função split serve para pegar somente a parte do código
anterior ao T"""
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
