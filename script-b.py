import requests
import csv

ips=[]
f = open('vm-infos.txt', 'r')
content = f.read()
contentList = content.replace('\n', ' ').split(" ")
for i in range (1,len(contentList)):
    if i % 2 != 0:
        ips.append(contentList[i])
print(ips)
#r = requests.get('https://api.github.com/user')

#print('IP: %s Response: %s ' %(,r.status_code))
