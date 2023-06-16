import requests
from pprint import pprint

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]


pprint(last_twenty_years[0]['value'])

for year in last_twenty_years:
    try:
        display_width = year["value"] // 10_000_000
        print(year['date'], '=' * display_width)
    except:
        print(year['date'], 'no data')
