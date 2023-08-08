import os
from flask import Flask, render_template
from flask_login import LoginManager
from api import api
from authentification import authentification
from user import User

appserver = Flask(__name__,
            static_folder = "../dist/static",
            template_folder="../dist")

login_manager = LoginManager(appserver)
login_manager.init_app(authentification)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

appserver.register_blueprint(api, url_prefix='/api')
appserver.register_blueprint(authentification, url_prefix='/auth')


appserver.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

@appserver.route('/', defaults={'path': ''})
@appserver.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == "__main__":
    appserver.run(debug=True)