from flask import Flask, jsonify, request


customers = [
             {
              "email": "jan.novak@example.cz",
              "username": "johny",
              "name": "Jan Novák",
              "newsletter_status": True,
              "trips": [
                            {
                             "destination": "Oslo, Norway",
                             "price": 150.00
                            },
                            {
                             "destination": "Bangkok, Thailand",
                             "price": 965.00
                            }
                          ]
             },
             {
              "email": "ivan.opletal@example.com",
              "username": "ivan123",
              "name": "Ivan Opletal",
              "newsletter_status": False,
              "trips": []
             }
        ]

app = Flask(__name__)


@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers), 200


@app.route('/customer/<string:username>', methods=['GET'])
def get_customer(username):
    for customer in customers:
        if customer['username'] == username:
            return jsonify(customer), 200
    return jsonify({'message': 'customer not found'}), 404


@app.route('/customer', methods=['POST'])
def create_customer():
    request_data = request.get_json()
    new_customer = {
        "email": request_data['email'],
        "username": request_data['username'],
        "name": request_data['name'],
        "newsletter_status": request_data['status'],
        "trips": []
    }
    for customer in customers:
        if customer['username'] == new_customer['username']:
            return jsonify({'error': 'username already exist'}), 409
    customers.append(new_customer)
    return jsonify(new_customer), 201


@app.route('/customer/<string:username>/trips', methods=['GET'])
def get_trips(username):
    for customer in customers:
        if customer['username'] == username:
            return jsonify({'trips': customer['trips']}), 201
    return jsonify({'error': 'username not found'}), 404


@app.route('/customer/<string:username>/trips', methods=['POST'])
def create_trip_for_user(username):
    for customer in customers:
        if customer['username'] == username:
            request_data = request.get_json()
            new_trip = {
                "destination": request_data['destination'],
                "price": request_data['price']
            }
            customer['trips'].append(new_trip)
            return new_trip, 201
    return jsonify({'error': 'username not found'}), 404


app.run(port=3333, debug=True)
