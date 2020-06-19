import requests, json

def shorterLink():
    apiKey = input("Your API key: ")
    url = input("Your URL: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    data = {"url": url}
    main = json.loads(requests.post("https://api.be-team.me/short_link",headers=headers,data=data).text)
    print("Link: "+ main["result"])

shorterLink()
