import requests, json

def cookPad():
    apiKey = "YOUR_APIKEY_HERE"
    url = "nastar"
    lang = "id" #[en,id]
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/cookpad?lang="+lang+"&search="+url,headers=headers).text)
    print(main)


cookPad()
