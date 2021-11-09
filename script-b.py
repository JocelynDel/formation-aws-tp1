import requests
import csv

ips=[]
f = open('vm-infos.txt', 'r')
content = f.read()
contentList = content.replace('\n', ' ').split(" ")
for i in range (1,len(contentList)):
    if i % 2 != 0:
        ips.append(contentList[i])
for i in ips:
    r = requests.get('http://%s:80' % i)
    print('IP: %s Response: %s' % (i,r))

#print('IP: %s Response: %s ' %(,r.status_code))
