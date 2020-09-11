import requests, json, time

def tempMail():
    apiKey = "YOUR_APIKEY_HERE" ## NEED VIP
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/tempmail",headers=headers).text)
    print("Your temporary gmail: "+main["result"]["email"])
    print("Waiting for messages...")
    read = []
    while True:
        result = json.loads(requests.get(main["result"]["callback"],headers=headers).text)
        for msg in result["result"]:
            if msg["id"] not in read:
                print("Subject: "+msg["subject"])
                print("Message Text: "+msg["text"])
                print("Message HTML: "+msg["html"])
                read.append(msg["id"])
        time.sleep(5)

tempMail()
