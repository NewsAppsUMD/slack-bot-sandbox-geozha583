import requests
import json
import os

congress_key = os.environ.get('CONGRESS_API_KEY')

url = f"https://api.congress.gov/v3/committee-report/119/hrpt?api_key={congress_key}&format=json"

r = requests.get(url)

results = r.json()



first_report = results["reports"][0]['url']

fr = requests.get(first_report + f"&api_key={congress_key}")

result = fr.json()

print(result)

for i in range(len(results["reports"])):
    if results["reports"][i]["number"] > 5:
        print(results["reports"][i]) #error here!