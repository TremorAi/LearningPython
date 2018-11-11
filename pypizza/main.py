__author__ = "Tremor"

from dominos.api import Client

api = Client
response = api.get_nearest_store('AB12 000')
print(response.json())
