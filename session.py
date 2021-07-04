import requests
import json
import uuid
import os
from os import system
system("title " + "Session ID")

username = input("Username: ")
password = input("Password: ")
uid = str(uuid.uuid4())
coo = ""
h = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com',
    'Connection': 'keep-alive'
}



def login():
    global h, coo
    url = "https://i.instagram.com/api/v1/accounts/login/"
    l = {'uuid': uid,
                  'password': password,
                  'username': username,
                  'device_id': uid,
                  'from_reg': 'false',
                  '_csrftoken': 'missing',
                  'login_attempt_count': '0'}
    login1 = requests.post(url, data=l, headers=h)
    login2 = login1.status_code
    if login2==200:
        SID = login1.cookies["sessionid"]
        print(f"Session ID: {SID}")
        input()
    else:
        print("Error")
        input()
        exit()


login()
