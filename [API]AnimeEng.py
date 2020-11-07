import requests, json

def AnimengMovie():
    apiKey = "YOUR_APIKEY_HERE"
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/animeng/movie",headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))
  
def AnimengSeries():
    apiKey = "YOUR_APIKEY_HERE"
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/animeng/series",headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

AnimengSeries()
