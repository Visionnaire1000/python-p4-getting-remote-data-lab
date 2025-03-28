from GetRequester import GetRequester

URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
CONVERTED_DATA = [
    {"name": "Daniel", "occupation": "LG Fridge Salesman"},
    {"name": "Joe", "occupation": "WiFi Fixer"},
    {"name": "Avi", "occupation": "DJ"},
    {"name": "Howard", "occupation": "Mountain Legend"},
]

def test_load_json():
    '''load_json function returns response.'''
    requester = GetRequester(URL)
    assert requester.load_json() == CONVERTED_DATA
