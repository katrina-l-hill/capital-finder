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

        if "capital" in dictionary:
            full_url = base_url + "capital/" + dictionary.get("capital")
            response = requests.get(full_url)
            data = response.json()
            capitals = data[0]["capital"]
            # joined_capitals = " and ".join(capitals)
            # for city_data in data:
            #     city_json_info = city_data["capital"][0]
            #     list_of_cities.append(city_json_info)
            # message = str(capitals)
            message = f"the capital of {country} is {capitals}"

        if country:
            response = requests.get(base_url + "name/" + country)
            data = response.json
            capital_response = data[0]["capital"]
            message = f"{capital_response} is the capital of {country}"
        else:
            message = "Type a city name to get info about it and the country"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
