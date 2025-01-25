import json
import boto3
client=boto3.client('ec2')

def lambda_handler(event, context):
    response=client.run_instances(
    ImageId='ami-01b799c439fd5516a',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1)
    
    
    print(response[Instances][0][InstanceId])