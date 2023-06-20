import requests
import json

url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
JSON_STRING = b"[\n  {\n    \"name\": \"Daniel\",\n    \"occupation\": \"LG Fridge Salesman\"\n  },\n  {\n    \"name\": \"Joe\",\n    \"occupation\": \"WiFi Fixer\"\n  },\n  {\n    \"name\": \"Avi\",\n    \"occupation\": \"DJ\"\n  },\n  {\n    \"name\": \"Howard\",\n    \"occupation\": \"Mountain Legend\"\n  }\n]\n"
CONVERTED_DATA = [{ 'name': 'Daniel', 'occupation' : 'LG Fridge Salesman' }, { 'name': 'Joe', 'occupation': 'WiFi Fixer' }, { 'name': 'Avi', 'occupation': 'DJ' }, { 'name': 'Howard', 'occupation': 'Mountain Legend' }]

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response = self.get_response_body()
        data = json.loads(response)
        return data
