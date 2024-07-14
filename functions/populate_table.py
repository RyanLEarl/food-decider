import json
import boto3

dynamodb = boto3.resource('dynamodb') 
table = dynamodb.Table('food-decider-dev-food-options')
restaurants = [
    ['Noi Thai', 'Asian', 1],
    ['Chi', 'Chinese', 1],
    ['Wonderland Chicken Co', 'American', 0],
    ['BOSA', 'Pasta', 0],
    ['Five Guys', 'American', 1],
    ['Blue Eyes Burgers & Fries', 'American', 1],
    ['Bogey\'s Burgers', 'American', 1],
    ['El Caporal', 'Mexican', 1],
    ['El Sancho Taco Shop', 'Mexican', 1],
    ['Wild Rose', 'Asian', 1],
    ['Spork', 'Asian', 1],
    ['Don Gabino\'s', 'Mexican', 0],
    ['Pho Viet', 'Asian', 1],
    ['Aloha Cafe', 'Hawaiian', 1],
    ['900 Wall', 'Fancy', 0],
    ['Parilla Grill', 'Mexican', 0],
    ['Brother Jon\'s', 'American', 0],
    ['The Blacksmith', 'Fancy', 0],
    ['Drake', 'Fancy', 1],
    ['Five Fusion', 'Sushi', 0],
    ['Pinky G\'s Pizzeria', 'Pizza', 1],
    ['Papa Murphy\'s', 'Pizza', 1],
    ['Cibelli\'s', 'Pizza', 1],
    ['Fire on the Mountain Buffalo Wings', 'American', 0],
    ['Northwest Wing Shop', 'American', 0],
    ['Miyagi Ramen', 'Ramen', 1],
    ['Mio Sushi', 'Sushi', 1],
    ['Juno Japanese Sushi Garden', 'Sushi', 0],
    ['10 Barrel Brewing', 'American', 1],
    ['Red Robin', 'American', 1],
    ['Croutons', 'Sandwiches', 1],
    ['New York City Sub Shop', 'Sandwiches', 1],
    ['Chow', 'Breakfast', 0],
    ['Jake\'s Diner', 'Breakfast', 1],
    ['Chipotle', 'Mexican', 1],
    ['Bend Breakfast Burrito', 'Breakfast', 0],
    ['The Corndog Company Of Central Oregon', 'American', 0],
    ['Longboard Louie\'s', 'Mexican', 1],
    ['Strictly Organic', 'Breakfast', 1],
    ['Big O Bagels', 'Breakfast', 0],
    ['Thump Coffee', 'Breakfast', 0],
    ['El Rodeo', 'Mexican', 0],
    ['Bigfoot Barbecue Co', 'American', 0],
    ['Dang\'s Vietnamese Restaurant', 'Asian', 0],
    ['The Tin Pig', 'American', 0],
    ['Big Island Kona Mix Plate', 'Hawaiian', 0],
    ['Immersion Brewing', 'American', 0],
    ['Papi Chulo\'s Taqueria', 'Mexican', 0],
    ['Tacos Pihuamo', 'Mexican', 0],
    ['Bluma\'s Chicken & Waffles', 'American', 0],
    ['Abe Capanna\'s Detroit Pan Pizza', 'Pizza', 0],
    ['Blind Tiger Pizza', 'Pizza', 0],
    ['MOD Pizza', 'Pizza', 0],
    ['Tradesmen Coffee and Taphouse', 'American', 0]
]

def handler(event, context):
    with table.batch_writer() as batch:
        for restaurant in restaurants:
            batch.put_item(
                Item={
                    'name': restaurant[0],
                    'food_type': restaurant[1],
                    'visited': restaurant[2]
                } 
            )
    # response = table.put_item( 
    #    Item={
    #         'name': 'Noi Thai',
    #         'food_type': 'Thai',
    #         'visited': 1
    #     } 
    # ) 
    # return response
    # print(event)