


def lambda_handler(event, context):
    print("Received event:", event)
    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully!'
    }