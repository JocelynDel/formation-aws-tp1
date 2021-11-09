import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

ids=[]
f = open('vm-infos.txt', 'r')
content = f.read()
contentList = content.replace('\n', ' ').split(" ")
for i in range (len(contentList)):
    if i % 2 == 0:
        ids.append(contentList[i])

ec2_client.terminate_instances(InstanceIds=ids)
print('EC2 instances are terminated')
