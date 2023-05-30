import json


import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
    http_method = event['httpMethod']
    if http_method == 'GET':
        return get_handler()
    elif http_method == 'POST':
        return post_handler(event['body'])
    elif http_method == 'PUT':
        return put_handler(event['body'])
    elif http_method == 'DELETE':
        return delete_handler(event['queryStringParameters'])
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid HTTP method')
        }


def get_handler():
    # Handle GET requests
    response = dynamodb.scan(TableName='MenuTable')
    items = response['Items']

    # Convert DynamoDB response items to a standard Python list
    data = []
    for item in items:
        data.append({
            'id': item['id']['S'],
            'name': item['name']['S'],
            'description': item['description']['S']
        })

    response_body = {
        'data': data
    }
    return {
        'statusCode': 200,
        'body': json.dumps(response_body)
    }


def post_handler(body):
    # Handle POST requests
    request_data = json.loads(body)
    item_id = request_data['id']
    item_name = request_data['name']
    item_description = request_data['description']

    # Add the new item to DynamoDB
    response = dynamodb.put_item(
        TableName='MenuTable',
        Item={
            'id': {'S': item_id},
            'name': {'S': item_name},
            'description': {'S': item_description}
        }
    )

    response_body = {
        'message': 'Resource created successfully',
        'data': request_data
    }
    return {
        'statusCode': 200,  # Created
        'body': json.dumps(response_body)
    }


# The put_handler and delete_handler functions remain the same

def put_handler(body):
    # Handle PUT requests
    request_data = json.loads(body)
    item_id = request_data['id']
    item_name = request_data['name']
    item_description = request_data['description']

    # Update the existing item in DynamoDB
    response = dynamodb.update_item(
        TableName='MenuTable',
        Key={'id': {'S': item_id}},
        UpdateExpression='SET #name = :name, #description = :description',
        ExpressionAttributeNames={'#name': 'name', '#description': 'description'},
        ExpressionAttributeValues={':name': {'S': item_name}, ':description': {'S': item_description}}
    )

    response_body = {
        'message': 'Resource updated successfully',
        'data': request_data
    }
    return {
        'statusCode': 200,
        'body': json.dumps(response_body)
    }


def delete_handler(query_params):
    # Handle DELETE requests
    item_id = query_params['id']

    # Remove the item from DynamoDB
    response = dynamodb.delete_item(
        TableName='MenuTable',
        Key={'id': {'S': item_id}}
    )

    response_body = {
        'message': 'Resource deleted successfully'
    }
    return {
        'statusCode': 200,
        'body': json.dumps(response_body)
    }
