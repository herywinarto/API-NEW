import requests, json, random

# APPNAME LIST: ( THIS APPNAME JUST FOR GET QR, IF FOR LOGIN U CAN USE OLDER ONE )
# "IOSIPAD\t10.10.0\tiPhone 8\t11.2.5"
# "CHROMEOS\t2.3.8\tChrome OS\t1"
# "DESKTOPWIN\t6.0.3\tWindows\t10"
# "DESKTOPMAC\t6.0.3\tMAC\t10.15"

def QRV2():
    apiKey = "YOUR_APIKEY_HERE"
    headers = {
        "apiKey":apiKey, ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
        "appName": "IOSIPAD\t10.5.2\tiPhone 8\t11.2.5", ## APPNAME, YOU CAN CUSTOMIZE IT
        "cert" : None, ## IF YOU WANT LOGIN WITH CERT
        "server": random.choice(["pool-1","pool-2"]), ## IP POOL SELECTION: pool-1 / pool-2 / vip(COMING SOON)
        "sysname": "BE-Team" ## SYSTEM NAME, YOU CAN CUSTOMIZE IT
        }
    main = json.loads(requests.get("https://api.be-team.me/qrv2",headers=headers).text)
    print("QR Link: " + main["result"]["qr_link"])
    print("Login IP: " + main["result"]["login_ip"])
    if not headers["cert"]:
        print("Callback Pincode: " + main["result"]["cb_pincode"])
        result = json.loads(requests.get(main["result"]["cb_pincode"],headers=headers).text)
        print("Your Pincode: " + result["result"])
    result = json.loads(requests.get(main["result"]["cb_token"],headers=headers).text)
    if result["status"] != 200:
        print("[ Error ] "+ result["reason"])
    else:
        print("Your Cert: " + result["result"]["cert"])
        print("Your Token: " + result["result"]["token"])
    
QRV2()
