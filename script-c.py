import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

ips=[]
f = open('vm-infos.txt', 'r')
content = f.read()
contentList = content.replace('\n', ' ').split(" ")
for i in range (1,len(contentList)):
    if i % 2 != 0:
        ips.append(contentList[i])