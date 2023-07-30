import requests
import configparser
import os
import time



config = configparser.ConfigParser()
config.read_file(open(r"Config.ini"))
cookie = str(config.get("auth","cookie"))

config.read_file(open(r"Config.ini"))


session = requests.Session()
session.cookies[".ROBLOSECURITY"] = cookie

req = session.post(
    url="https://auth.roblox.com/"
)

if "X-CSRF-Token" in req.headers:  
    session.headers["X-CSRF-Token"] = req.headers["X-CSRF-Token"]  


req2 = session.post(
    url="https://auth.roblox.com/"
)


totaltrades = 0
totaltrades3 = 0




def inbounds():
    while True:
        try:
            def program():
                global totaltrades
                global progress
                progress = 0
                
                
                count = session.get("https://trades.roblox.com/v1/trades/Inbound/count")
                count2 = count.json()
                totaltrades = count2['count']
                
                
                Recent = session.get("https://trades.roblox.com/v1/trades/Inbound?sortOrder=Desc&limit=10")
                Recent2 = Recent.json()
                trade = Recent2['data'][0]['id']
                
                
                post1 = session.post(f"https://trades.roblox.com/v1/trades/{trade}/decline")
                progress += 1
                print(f"Deleted: {progress}/{totaltrades}")
            program()
            
        
        except:
            if progress == totaltrades:
                print("[SUCCESS] Declined all your INBOUND trades")
                print("")
                inputs()


def outbounds():
    while True:
        try:
            def program2():
                global totaltrades3
                global progress2
                progress2 = 0
                
                
                outbound_trades = session.get("https://trades.roblox.com/v1/trades/outbound")
                outbound_trades_json = outbound_trades.json()
                totaltrades3 = len(outbound_trades_json['data'])
                
                
                for trade_data in outbound_trades_json['data']:
                    trade_id = trade_data['id']

                    
                    post1 = session.post(f"https://trades.roblox.com/v1/trades/{trade_id}/decline")
                    progress2 += 1
                    print(f"Deleted: {progress2}/{totaltrades3}")
                
                
            program2()
            
        
        except:
            if progress2 == totaltrades3:
                print("[SUCCESS] Declined all your OUTBOUND trades")
                print("")
                inputs()



def inputs():
    print("[1] Inbounds\n[2] Outbounds\n")
    ask = int(input("Method: "))

    if ask == 1:
        inbounds()
    elif ask == 2:
        outbounds()
    elif ask > 2:
        print("[ERROR] You must enter either 1 or 2")
        inputs()
    else:
        print("[ERROR] You must enter either 1 or 2")
        inputs()


inputs()    
