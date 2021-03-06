from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

# Code base referenced from lecture

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)
        # base_url = "https://restcountries.com/v3.1/capital/"
        base_url = "https://restcountries.com/v3.1/"
        capital = dictionary.get("capital")
        country = dictionary.get("country")

        if capital:
            response = requests.get(base_url + "capital/" + capital)
            data = response.json()
            capitals = data[0]["capital"]
            country_name = data[0]["name"]["common"]
            message = f"the capital of {country_name} is {capitals[0]}"

        elif country:
            response = requests.get(base_url + "name/" + country)
            data = response.json()
            capital_response = data[0]["capital"]
            message = f"{capital_response[0]} is the capital of {country}"
        else:
            message = "Type a city name to get info about it and the country"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
