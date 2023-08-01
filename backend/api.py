from flask import Blueprint, app, jsonify, render_template

api = Blueprint('api', __name__)

@api.route('/hello')
def hello():
    response = {'msg': 'world'}
    return jsonify(response)