from flask import Blueprint, app, jsonify, render_template
from flask_login import login_required

api = Blueprint('api', __name__)

@api.route('/hello')
@login_required
def hello():
    response = {'msg': 'world'}
    return jsonify(response)