from flask import jsonify, request
from flask_restful import Resource

class SHORT_URL(Resource):
    def get(self, url=None):
        if url == None:
            return jsonify(status = "400 Bad-Request")
        else:
            return jsonify(status = "200 Ok", redirect = url)

    def post(self, url=None):
        original = request.form.get("original")
        short = request.form.get("short")

        data = {
            'original': original,
            'short': short 
        }

        return jsonify(status = "200 Ok", task = "resource created", data = data)

    def put(self, url=None):
        original = request.form.get("original")
        short = request.form.get("short")

        data = {
            'original': original,
            'short': short 
        }

        return jsonify(status = "200 Ok", task = "resource modified", data = data)

    def delete(self, url=None):
        original = request.form.get("original")
        short = request.form.get("short")

        data = {
            'original': original,
            'short': short 
        }

        return jsonify(status = "200 Ok", task = "resource destroyed", data = data)




    