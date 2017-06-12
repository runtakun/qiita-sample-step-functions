import boto3
import uuid
import os


def lambda_handler(event, context):
    account_id = event.get('account')

    state_machine_arn = 'arn:aws:states:us-east-1:%s:stateMachine:%s'\
                        % (account_id, os.environ.get("STATE_MACHINE_NAME"))
    client = boto3.client('stepfunctions', region_name='us-east-1')
    resp = client.start_execution(
        stateMachineArn=state_machine_arn,
        name=str(uuid.uuid4()),
    )

    return 'invoked step functions'
