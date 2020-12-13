from BEApi import *


api = BEApi("APIKEY_HERE")
result = api.oneCakRandom()
api.pretyPrintJson(result)
