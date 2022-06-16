from email.policy import default
from readline import get_current_history_length
import requests

    #api call
def get_currency_code_map():
    url_host = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.min.json"
    endpoint = "currencies"
    ext = ".min.json"
    url = url_host + endpoint + ext
    response = request.get(url)
    if response.ok:
        currency_code_map = response.json()
    else:
    currency_code_map = {
    "usd": "United States dollar",
    "usdc": "USD Coin",
    "usdp": "USDP Stablecoin",
    "cad": "Canadian dollar",
    "jpy": "Japanese yen",
    "eur": "Euro",
    }
    return.ok, currency_code_map
    
def get_exchange_rate(from_code, to_code):
    url_host = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.min.json"
    endpoint = from_code +"/" + to_code
    ext = ".json"
    url = url_host + endpoint + extresponse = request.get(url)
        if response.ok:
            exchange = response.json()
            rate = exchange[to_code]
        else:
            rate = 0
        return response.ok, rate

def get_currencies():
    currency_strings = []

    for code in currency_code_map.keys():
        currency = currency_code_map[code]
        currency_strings.append(code + " - " + currency)
    return currency_strings

def get_currency_from_code(code):
    return currency_code_map[code]

def get_currency_string(code):
    return code + " - " + get_currency_from_code(code)

success, currency_code_map = get_current_code_map

currencies = get_currencies()
default_from = get_currency_string("usd")
default_to = get_currency_string("eur")

if __name__=="__main__":
    get_currencies(currency_code_map)

    success, rate = get_exchange_rate("usd", "eur")
    print(rate)
