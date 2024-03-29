from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from keys import apikey
import datetime
from datetime import date, timedelta


#TODO: Colocar em funções todo esse código, de maneira responsiva.
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
#parâmetros exigidos pela URL do API do coinmarket; significa que ele analise as últimas 100 moedas mais atualizadas e usa o USD como a moeda padrão.""
parameters = {
  'start':'1',
  'limit':'100',
  'convert':'USD'
}

#Aqui estão os headers do link, incluindo a chave pessoal de cada desenvolvedor. Por razões de segurança, eu, Daniel Saldanha,
#escondi minha chave em um arquivo pessoal. Caso deseje utilizar esta API com este código, é necessário criar uma própria.
#Para mais informações de como criar sua própria chave, acesse: https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': apikey,
}

session = Session()
session.headers.update(headers)

first_price = input("diga-me em símbolo (ex: Bitcoin = BTC, ethereum = ETH) de qual moeda você deseja converter:")
first_price = first_price.upper()
second_price = input("diga-me em símbolo (ex: Bitcoin = BTC, ethereum = ETH) para qual moeda você deseja converter:")
second_price = second_price.upper()

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)

#A API do coinmarket devolve um JSON, o que no python é o mesmo que um dicionário e podemos explorá-lo desta forma.
#Para entender melhor o JSON que a API devolve, é interessante ir no site: https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
  for entry in data['data']:
    if entry['symbol'] == first_price:
      first_price_num = round(entry['quote']['USD']['price'], 3)
      print(f"o atual preço de {first_price} é: {first_price_num}")
    else:
      pass

  for entry in data['data']:     
    if entry['symbol'] == second_price:
      second_price_num = round(entry['quote']['USD']['price'], 3)
      print(f"o atual preço de {second_price} é: {second_price_num}")
    else:
      pass
  
  qunt = float(input("diga-me quanto você quer converter da primeira moeda:"))
  qunt_dol = first_price_num*qunt
  qunt_end = round(qunt_dol/second_price_num, 3)
  print(f"... \n {qunt} {first_price} equivalem a: {qunt_dol} USD \n... Sendo 1 {second_price} = {second_price_num}\n {qunt} {first_price} equivale a {qunt_end} {second_price}")

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#  --------------------------------------------
#Some possible changes, translated to english:

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from keys import apikey

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'100',
  'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': apikey,
}

session = Session()
session.headers.update(headers)

first_price = input("Enter the symbol of the currency you want to convert from:")
first_price = first_price.upper()
second_price = input("Enter the symbol of the currency you want to convert to:")
second_price = second_price.upper()

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)

  for entry in data['data']:
    if entry['symbol'] == first_price:
      first_price_num = round(entry['quote']['USD']['price'], 3)
      print(f"The current price of {first_price} is: {first_price_num} USD")
    else:
      pass

  for entry in data['data']:     
    if entry['symbol'] == second_price:
      second_price_num = round(entry['quote']['USD']['price'], 3)
      print(f"The current price of {second_price} is: {second_price_num} USD")
    else:
      pass
  
  qunt = float(input("Enter the amount you want to convert from the first currency:"))
  qunt_dol = first_price_num*qunt
  qunt_end = round(qunt_dol/second_price_num, 3)
  print(f"\n {qunt} {first_price} is equivalent to: {qunt_dol} USD \n 1 {second_price} is equal to {second_price_num} USD \n {qunt} {first_price} is equivalent to {qunt_end} {second_price}")

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
