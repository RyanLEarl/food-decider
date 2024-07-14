import boto3
import random
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb') 
table = dynamodb.Table('food-decider-dev-food-options')
restaurants = []

def handler(event, context):
    food_type = event.get('food_type', 'ALL')
    visited = event.get('visited', 'ALL')

    query = {}
    index_name = None

    if food_type != 'ALL':
        query['KeyConditionExpression'] = Key('food_type').eq(food_type)
        index_name = 'food_type-index'

    if visited != 'ALL':
        if 'KeyConditionExpression' in query:
            query['KeyConditionExpression'] = query['KeyConditionExpression'] & Key('visited').eq(visited)
            index_name = 'visited-index'
        else:
            query['KeyConditionExpression'] = Key('visited').eq(visited)
            index_name = 'visited-index'

    if index_name:
        query['IndexName'] = index_name

    if query:
        response = table.query(**query)
    else:
        response = table.scan()
    items = response['Items']
    random_item = random.choice(items)

    return random_item['name']