from flask import jsonify


def response(success, msg):
    return jsonify(msg), 200 if success else 418


# def response(t):
#     return response(t[0], t[1])
