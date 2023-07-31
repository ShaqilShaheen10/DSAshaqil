RestAPI

Python Code:

import requests

def findCountry(region, keyword):
    base_url = f"https://jsonmock.hackerrank.com/api/countries/search?region={region}&name={keyword}"
    response = requests.get(base_url)
    data = response.json()

    # Extracting relevant data from the API response
    records = data["data"]
    sorted_records = sorted(records, key=lambda x: (x["population"], x["name"]))

    # Format the result as required
    result = []
    for record in sorted_records:
        country_population = f"{record['name']}, {record['population']}"
        result.append(country_population)

    # Join the elements with newline character to print on different lines
    output = "\n".join(result)
    return output

# Test the function with the given input
region = "Europe"
keyword = "de"
output = findCountry(region, keyword)
print(output)
