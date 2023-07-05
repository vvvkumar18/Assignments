from flask import Flask, jsonify, request

app = Flask(__name__)
food  = [
    {
        'name': 'starters',
        'items': [
            {
                'name': 'chicken65',
                'price': 250
            }
        ]
    },
    {
        'name': 'biryani',
        'items': [
            {
                'name': 'chicken Biryani',
                'price': 350
            }
        ]
    },
    {
        'name': 'Dessert',
        'items': [
            {
                'name': 'junnu',
                'price': 120
            }
        ]
    },
    {
         'name': 'curry',
         'items': [
            {
                'name': 'chcicken curry',
                'price': 150
            }
         ]
    }

    
]



travel  = [
    {
        'name': 'vizag',
        'type': [
            {
                'name': 'train',
                'price': 250
            }
        ]
    },
    {
        'name': 'hyd',
        'type': [
            {
                'name': 'train ',
                'price': 350
            }
        ]
    },
    {
        'name': 'pune',
        'type': [
            {
                'name': 'flight',
                'price': 14000
            }
        ]
    },
    {
         'name': 'chennai',
         'type': [
            {
                'name': 'train ',
                'price': 1500
            }
         ]
    }

    
]


@app.route('/')
def home():
    return "Hello to Api"

@app.route('/food/<string:name>')
def get_food(name):
    for foods in food:
        if(foods['name'] == name):
            return jsonify(foods['name'])
    return jsonify({'message': 'food is not found'})

@app.route('/food/<string:name>/item')
def get_food_item(name):
    for foods in food:
        if(foods['name'] == name):
            return jsonify(foods['items'])
    return jsonify({'message': 'store not found'})


@app.route('/food')
def get_all_foods():
    return jsonify({'food': food})

#Post method
@app.route('/food', methods=['POST'])
def food_details():
    request_data = request.get_json()
    food_add = {
        'name': request_data['name'],
        'items': []
    }
    food.append(food_add)
    return jsonify(food_add)

@app.route('/food/<string:name>/item', methods=['POST'])
def food_items(name):
    request_data = request.get_json()
    for foods in food:
        if(foods['name'] == name):
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            foods['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})




@app.route('/travel/<string:name>')
def travel_details(name):
    for travels in travel:
        if(travels['name'] == name):
            return jsonify(travels['name'])
    return jsonify({'message': 'food is not found'})

@app.route('/travel/<string:name>/item')
def get_details(name):
    for travels in travel:
        if(travels['name'] == name):
            return jsonify(travels['type'])
    return jsonify({'message': 'store not found'})


@app.route('/travel')
def get_all_travels():
    return jsonify({'travel': travel})











app.run(port=5000)