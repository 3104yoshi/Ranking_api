from flask import Flask, app, render_template
from api import api

appserver = Flask(__name__,
            static_folder = "../dist/static",
            template_folder="../dist")

appserver.register_blueprint(api, url_prefix='/api')

@appserver.route('/', defaults={'path': ''})
@appserver.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == "__main__":
    appserver.run(debug=False)