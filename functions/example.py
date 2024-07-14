import boto3
import random
import json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb') 
table = dynamodb.Table('food-decider-dev-food-options')
restaurants = []

def handler(event, context):
    body = json.loads(event['body'])
    print(body)
    food_type = body.get('food_type', 'ALL')
    visited = body.get('visited', 'ALL')

    if visited.lower() == 'yes':
        visited = 1
    elif visited.lower() == 'no':
        visited = 0

    print (food_type, visited)

    query = {}
    index_name = None

    if food_type != 'ALL' and visited != 'ALL':
        query['KeyConditionExpression'] = Key('food_type').eq(food_type) & Key('visited').eq(visited)
        index_name = 'food_type-visited-index'
    elif visited != 'ALL':
        query['KeyConditionExpression'] = Key('visited').eq(visited)
        index_name = 'visited-index'

    if query:
        query['IndexName'] = index_name
        print(query)
        response = table.query(**query)
    else:
        response = table.scan()
    items = response['Items']
    random_item = random.choice(items)
    response = {
        "statusCode": 200,
        "body": random_item['name']
    }
    print(response)
    return response
