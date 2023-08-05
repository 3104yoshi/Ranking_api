from distutils.util import strtobool
from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import flask_login
from db.accessor.userCredentialAccessor import userCredentialAccessor
from user import User
from db.data.userCredential import userCredential


authentification = Blueprint('authentification', __name__)

@authentification.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')

    username = request.form.get('username')
    password = request.form.get('password')

    credential = userCredential(username, password)
    fetchedUser = userCredentialAccessor.getUser(credential)
    is_authentificated = len(fetchedUser) == 1

    if is_authentificated:
        user = User(username)
        flask_login.login_user(user)
        return redirect(url_for('api.hello'))

    return render_template('index.html')


@authentification.route('/Signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('index.html')

    username = request.form.get('username')
    password = request.form.get('password')

    credential = userCredential(username, password)
    fetchedUser = userCredentialAccessor.checkUserIs(credential)
    if len(fetchedUser) == 1:
        return jsonify({'canSignup': False})

    userCredentialAccessor.addUser(credential)

    return redirect(url_for('authentification.canSignup', canSignup=True))


@authentification.route('/CanSignup/<canSignup>/', methods=['GET', 'POST'])
def canSignup(canSignup):
    if strtobool(canSignup):
        return render_template('index.html')
    return redirect(url_for('authentification.signup'))


@authentification.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/Login')
