# from flask import Flask
#
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET'])
# def home():
#     return 'Hello Flask'
#
#
# app.run(port=3333, debug=True)

from flask import Flask, escape, request


app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


app.run(port=3333)
