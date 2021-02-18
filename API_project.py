from flask import Flask, jsonify


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


app.run(port=3333, debug=True)
