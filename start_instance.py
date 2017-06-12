import boto3
import base64


def lambda_handler(event, context):
    client = boto3.client('ec2', region_name='us-east-1')
    resp = client.run_instances(
        ImageId='ami-898b1a9f',
        MinCount=1,
        MaxCount=1,
        KeyName='runtakun_us-east-1.pem',
        SecurityGroups=['default', 'ssh'],
        UserData=_make_user_data(),
        InstanceType='m3.medium',
        IamInstanceProfile={
            'Name': 'ssm-role',
        },
    )

    event['instance_id'] = resp['Instances'][0]['InstanceId']

    return event

def _make_user_data():
    with open('user-data.txt', 'rb') as f:
        return base64.b64encode(f.read())
