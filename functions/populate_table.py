import json
import boto3

dynamodb = boto3.resource('dynamodb') 
table = dynamodb.Table('food-decider-dev-food-options')
restaurants = [
    ['Noi Thai', 'Asian', 1, 'https://noithaiselect.com/menu?utm_source=google&location=noithaicuisinebend'],
    ['Chi', 'Chinese', 1, 'https://order.spoton.com/so-chi-chinese-and-sushi-bar-17469/bend-or/65cab034b7bc691c2899d9c0'],
    ['Wonderland Chicken Co', 'American', 0, 'https://order.toasttab.com/online/wonderland-chicken-bunk-brew-42-nw-hawthorne-ave'],
    ['BOSA', 'Pasta', 0, 'https://www.bosabend.com/menus/'],
    ['Five Guys', 'American', 1, 'https://order.fiveguys.com/location/five-guys-bend/menu'],
    ['Blue Eyes Burgers & Fries', 'American', 1, 'https://order.blueeyesburgersandfries.com/order/blue-eyes-burger-and-fries-truck'],
    ['Bogey\'s Burgers', 'American', 1, 'https://bogeysburgers.com/menu/'],
    ['El Caporal', 'Mexican', 1, 'https://www.elcaporalco.com/bend'],
    ['El Sancho Taco Shop', 'Mexican', 1, 'https://www.elsanchobend.com/menu/#menu'],
    ['Wild Rose', 'Asian', 1, 'https://www.wildrosethai.com/#menus'],
    ['Spork', 'Asian', 1, 'https://www.sporkbend.com/menu'],
    ['Don Gabino\'s', 'Mexican', 0, 'https://www.ordertakeouttoday.com/order/restaurant/don-gabinos-mexican-grill-menu/20432'],
    ['Pho Viet', 'Asian', 1, 'http://phovietandcafe.com/openmenu/main-menu'],
    ['Aloha Cafe', 'Hawaiian', 1, 'https://www.alohacafebbq.com/menus/'],
    ['900 Wall', 'Fancy', 0, 'https://www.900wall.com/900-wall-dinner-menu'],
    ['Parilla Grill', 'Mexican', 0, 'https://www.parrillagrill-bend.com/menu'],
    ['Brother Jon\'s', 'American', 0, 'https://www.brotherjonspublichouse.com/food'],
    ['The Blacksmith', 'Fancy', 0, 'https://bendblacksmith.com/dinner-menu/'],
    ['Drake', 'Fancy', 1, 'https://www.drakebend.com/dinner'],
    ['Five Fusion', 'Sushi', 0, 'https://www.5fusion.com/menu'],
    ['Pinky G\'s Pizzeria', 'Pizza', 1, 'https://pinkygs.com/bend-menu/'],
    ['Papa Murphy\'s', 'Pizza', 1, 'https://locations.papamurphys.com/or/bend/2155-ne-hwy-20'],
    ['Cibelli\'s', 'Pizza', 1, 'https://cibellis.com/menu/'],
    ['Fire on the Mountain Buffalo Wings', 'American', 0, 'https://storage.googleapis.com/public.fotmwings.com/menus/fotm_bend_menu.pdf'],
    ['Northwest Wing Shop', 'American', 0, 'https://places.singleplatform.com/northwest-wing-shop/menu?ref=google'],
    ['Miyagi Ramen', 'Ramen', 1, 'https://static1.squarespace.com/static/6233bc6651b70f02dcaa3c74/t/658cc9fbf9269a2f11b6e645/1703725564396/Miyagi+Menu+CURRENT+FINAL.pdf'],
    ['Mio Sushi', 'Sushi', 1, 'https://www.miosushi.com/bend-menu'],
    ['Juno Japanese Sushi Garden', 'Sushi', 0, 'https://www.seamless.com/menu/juno-japanese-sushi-garden-536-nw-arizona-ave-bend/7904472'],
    ['10 Barrel Brewing', 'American', 1, 'https://10barrel.com/wp-content/uploads/2020/05/Westside-Food-Menu-5.3.24.pdf'],
    ['Red Robin', 'American', 1, 'https://www.redrobin.com/location/red-robin-bend/menu'],
    ['Croutons', 'Sandwiches', 1, 'https://www.ordertakeouttoday.com/order/restaurant/croutons-bend-menu/14748'],
    ['New York City Sub Shop', 'Sandwiches', 1, 'https://www.nycss.com/menu'],
    ['Chow', 'Breakfast', 0, 'https://www.bendinspoon.com/'],
    ['Jake\'s Diner', 'Breakfast', 1, 'https://jakesdinerbend.com/menu'],
    ['Chipotle', 'Mexican', 1, 'https://locations.chipotle.com/or/bend/222-ne-emerson-ave'],
    ['Bend Breakfast Burrito', 'Breakfast', 0, 'https://www.bendbreakfastburrito.com/new-page'],
    ['The Corndog Company Of Central Oregon', 'American', 0, 'https://thecorndogco.com/menu.html'],
    ['Longboard Louie\'s', 'Mexican', 1, 'https://longboardlouies.com/menu/'],
    ['Strictly Organic', 'Breakfast', 1, 'https://www.strictlyorganic.com/page-2'],
    ['Big O Bagels', 'Breakfast', 0, 'https://www.bigobagels.com/menu'],
    ['Thump Coffee', 'Breakfast', 0, 'https://static1.squarespace.com/static/5c4f8fd25417fc08ead64cd9/t/5c89cdfa9140b7d7eeabb374/1552535042080/Thump+York+Coffee+Food+Menu.pdf'],
    ['El Rodeo', 'Mexican', 0, 'https://elrodeobend.com/menu/'],
    ['Bigfoot Barbecue Co', 'American', 0, 'https://www.foodtruckbend.com/'],
    ['Dang\'s Vietnamese Restaurant', 'Asian', 0, 'http://dangsvietnameserestaurant.com/menu/'],
    ['The Tin Pig', 'American', 0, 'https://thetinpigfoodcart.com/menu'],
    ['Big Island Kona Mix Plate', 'Hawaiian', 0, 'https://konamixplate.com/'],
    ['Immersion Brewing', 'American', 0, 'https://imbrewing.com/wp-content/uploads/2024/06/Menu-6.4.pdf'],
    ['Papi Chulo\'s Taqueria', 'Mexican', 0, 'https://www.papichulospdx.com/fullmenu'],
    ['Tacos Pihuamo', 'Mexican', 0, 'https://www.zmenu.com/tacos-pihuamo-bend-2-online-menu/'],
    ['Bluma\'s Chicken & Waffles', 'American', 0, 'https://blumas-chicken-waffles-old-mill.square.site/#items'],
    ['Abe Capanna\'s Detroit Pan Pizza', 'Pizza', 0, 'https://abe-capannas-detroit-pan-pizza-italian.square.site/'],
    ['Blind Tiger Pizza', 'Pizza', 0, 'https://www.blindtigerpizza.co/#3'],
    ['MOD Pizza', 'Pizza', 0, 'https://modpizza.com/menu/'],
    ['Tradesmen Coffee and Taphouse', 'American', 0, 'https://www.tradesmencoffeetaphouse.com/']
]

def handler(event, context):
    with table.batch_writer() as batch:
        for restaurant in restaurants:
            batch.put_item(
                Item={
                    'name': restaurant[0],
                    'food_type': restaurant[1],
                    'visited': restaurant[2],
                    'menu': restaurant[3],
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