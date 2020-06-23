import requests, json, random

def primary2Secondary():
    apiKey = input("Your API key: ")
    authToken = input("Your Primary Token: ")
    headers = {
        "apiKey": apiKey, ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
        "appName": "IOSIPAD\t10.5.2\tiPhone 8\t11.2.5", ## APPNAME, YOU CAN CUSTOMIZE IT
        "server": random.choice(["pool-1","pool-2"]), ## IP POOL SELECTION: pool-1 / pool-2 / vip(COMING SOON)
        "sysname": "BE-Team", ## SYSTEM NAME, YOU CAN CUSTOMIZE IT
        "authToken": authToken## YOUR PRIMARY TOKEN
        }
    main = json.loads(requests.get("https://api.be-team.me/primary2secondary",headers=headers).text)
    if main["status"] != 200:
        print("[ Error ] " + main["reason"])
    else:
        print("Login IP: " + main["result"]["login_ip"])
        print("Your Token: " + main["result"]["token"])
    
    
primary2Secondary()
