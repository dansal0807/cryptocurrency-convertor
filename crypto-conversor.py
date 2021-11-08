from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from keys import apikey
import datetime
from datetime import date, timedelta

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

first_price = input("diga-me em símbolo (ex: Bitcoin = BTC, ethereum = ETH) de qual moeda você deseja converter:")
first_price = first_price.upper()
second_price = input("diga-me em símbolo (ex: Bitcoin = BTC, ethereum = ETH) para qual moeda você deseja converter:")
second_price = second_price.upper()

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)

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
  
  qunt = float(input("diga-me quanto você quer converter(da primeira moeda):"))
  qunt_dol = first_price_num*qunt
  qunt_end = round(qunt_dol/second_price_num, 3)
  print(f"... \n {qunt} {first_price} equivalem a: {qunt_dol} USD \n... Sendo 1 {second_price} = {second_price_num}\n {qunt} {first_price} equivale a {qunt_end} {second_price}")




  
  """print("o preço do bitcoin está:")
  print((data['data'][0]['symbol']), round(data['data'][0]['quote']['USD']['price'], 2))

  print('o preço do ethereum está:')
  print((data['data'][1]['symbol']), round(data['data'][1]['quote']['USD']['price'], 2))"""

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)