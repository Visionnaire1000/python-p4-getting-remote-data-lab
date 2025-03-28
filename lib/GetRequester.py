import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text.strip()  # Strip any leading/trailing whitespace or newlines

    def load_json(self):
        return json.loads(self.get_response_body())  # Convert JSON string to Python dict or list

# Example usage:
if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)
    
    print(requester.get_response_body())  # Raw JSON response
    print(requester.load_json())  # Parsed JSON data
