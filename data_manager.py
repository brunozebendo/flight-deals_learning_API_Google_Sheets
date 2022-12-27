from pprint import pprint
"""The pprint module in Python is a utility module that you can use to print data structures in a readable,
 pretty way. It’s a part of the standard library that’s especially useful for debugging code dealing 
 with API requests, large JSON files, and data in general. Traduzindo, pprint é uma biblioteca interna do
 Python, já instalada por padrão, que imprime os dados de um JSON de forma mais visível. Existem
 sete formas de impressão, conforme explicado no site do real python """
import requests
"""aqui deve ser preenchido o endpoint da planilha do Googledocs"""
SHEETY_PRICES_ENDPOINT = YOUR SHEETY PRICES ENDPOINT

"""essa classe vai lidar com os dados no GoogleSheet, primeiro cria um destination_data como uma lista
vazia, depois obtem o preço da passagem de cada cidade, e a segunda função atualiza o preço de cada cidade
através da função put do json"""
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
