import requests, json

def GoogleImage():
    apiKey = input("Your API key: ")
    search = input("Your Search Query: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/googleimg?search="+search,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

GoogleImage()
