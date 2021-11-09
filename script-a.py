import boto3

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 

f = open('vm-infos.txt', 'w')
user_data_content = """#!/bin/bash
sudo apt update -y
sudo apt install -y ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update -y
sudo apt install -y docker-ce docker-ce-cli containerd.io 
sudo docker run -d -p 80:80 --name my-apache-app httpd"""

numVm = inputNumber("Numbers of VM to create? ")
ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')
info = {}

for i in range (1, numVm+1):
    ec2_instance = ec2_resource.create_instances(
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/xvda',
                'Ebs': {
                    'DeleteOnTermination': True,
                    'VolumeSize': 8,
                    'VolumeType': 'gp2',
                },
            },
        ],
        ImageId='ami-0a49b025fffbbdac6',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        UserData=user_data_content,
        SecurityGroupIds=[
            'sg-039f72687978812c8',
        ],
        Monitoring={'Enabled':False},
    )

    ec2_instance_id = ec2_instance[0].id
    print('Creating EC2 instance')
    waiter = ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[ec2_instance_id])
    print('EC2 Instance created successfully with ID: ' + ec2_instance_id)
    ec2_instance[0].reload()
    ec2_instance_ip = ec2_instance[0].public_ip_address
    info[ec2_instance_id] = ec2_instance_ip
    #print(info.items())
f.write('\n'.join('%s %s' % x for x in info.items()))