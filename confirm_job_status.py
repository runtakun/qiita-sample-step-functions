import boto3


def lambda_handler(event, context):
    client = boto3.client('ssm', region_name='us-east-1')

    resp = client.get_command_invocation(
        CommandId=event['command_id'],
        InstanceId=event['instance_id'],
    )

    event['job_status'] = resp['Status']

    return event
