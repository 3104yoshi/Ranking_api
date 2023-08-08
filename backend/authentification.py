from distutils.util import strtobool
from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import flask_login
from db.accessor.userCredentialAccessor import userCredentialAccessor
from user import User
from db.data.userCredential import userCredential


authentification = Blueprint('auth', __name__)

@authentification.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')

    username = request.form.get('username')
    password = request.form.get('password')

    credential = userCredential(username, password)
    fetchedUser = userCredentialAccessor.getUser(credential)

    if len(fetchedUser) == 1:
        user = User(username)
        flask_login.login_user(user)
        return redirect(url_for('api.hello'))

    return render_template('index.html')


@authentification.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('index.html')

    username = request.form.get('username')
    password = request.form.get('password')

    credential = userCredential(username, password)
    fetchedUser = userCredentialAccessor.checkUserIs(credential)
    if len(fetchedUser) == 1:
        return redirect(url_for('auth.canSignup', canSignup="既に登録されているユーザー名です"))

    userCredentialAccessor.addUser(credential)

    return redirect(url_for('auth.canSignup', canSignup="登録に成功しました"))


@authentification.route('/canSignup/<canSignup>/', methods=['GET', 'POST'])
def canSignup(canSignup):
    return render_template('index.html', signupStatus=canSignup)


@authentification.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/Login')
