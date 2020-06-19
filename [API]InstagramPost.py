import requests, json

def InstaPost():
    apiKey = input("Your API key: ")
    url = input("Your InstagramPost URL: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/instapost?url="+url,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))


InstaPost()
