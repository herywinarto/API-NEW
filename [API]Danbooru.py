import requests, json

def DanbooruPage():
    apiKey = "YOUR_APIKEY_HERE"
    page = "1" ## EXAMPLE PAGE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/danbooru?page="+page,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

DanbooruPage()
