from flask import Flask, jsonify
from flask_restful import Api

from resources.short_url import SHORT_URL

app = Flask(__name__)
api = Api(app)

api.add_resource(SHORT_URL, "/url/<string:url>", "/url")

if __name__ == '__main__':
    app.run(debug=True, port=8080)