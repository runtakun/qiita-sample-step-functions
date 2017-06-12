import boto3


def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    instance = ec2.Instance(event['instance_id'])
    resp = instance.terminate()

    return event
