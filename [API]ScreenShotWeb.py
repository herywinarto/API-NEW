import requests, json

def SSWeb():
    apiKey = input("Your API key: ")
    url = input("Your URL: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/ssweb?url="+url,headers=headers).text)
    print("Link: "+ main["result"])


SSWeb()
