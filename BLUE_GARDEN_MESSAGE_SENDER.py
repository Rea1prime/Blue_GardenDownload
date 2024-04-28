import requests
import time


#My server -> https://discord.com/api/v9/channels/1142594881299173418/messages
#Blue Garden Server -> https://discord.com/api/v8/channels/1233155342272299059/messages

payload = {
    "content": "[+] -> Request.post sent successfully"
}
print("[+] -> Payload loaded")
header = {
    "authorization": "ODQwMjEzMzA3ODEzMjY1NDI5.GP8z6S.y3CbHN9X-c8NOctuj4kBitnq2BRnxXU4VpjgiE"
}
print("[+] -> Header loaded")
try:
    r = requests.post("https://discord.com/api/v9/channels/1142594881299173418/messages", data=payload, headers=header)
    print("[+] -> Request.post sent successfully")
except Exception as e:
    print(e)
    time.sleep(9999)
    print("[-] -> Request.post failed to send")

