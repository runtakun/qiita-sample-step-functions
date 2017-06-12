import boto3


def lambda_handler(event, context):
    client = boto3.client('ssm', region_name='us-east-1')

    command = "docker run --log-driver=awslogs" \
              " --log-opt awslogs-group=hello-world" \
              " --log-opt awslogs-region=us-east-1 --rm" \
              " -i alpine:latest /bin/echo 'hello, world'"

    resp = client.send_command(
        InstanceIds=[event['instance_id']],
        DocumentName='AWS-RunShellScript',
        MaxConcurrency='1',
        Parameters={
            'commands': [
                "yum install -y docker",
                "service docker start",
                "eval $(aws ecr get-login --no-include-email --region us-east-1)",
                command,
            ],
        },
        TimeoutSeconds=3600,
    )

    event['command_id'] = resp['Command']['CommandId']

    return event
