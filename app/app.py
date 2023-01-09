from flask import Flask

from blueprints import webui
from extensions import config, login_manager, jinja_filters


if __name__ == '__main__':
    
    app = Flask(__name__)

    webui.init_app(app)
    config.init_app(app)    
    login_manager.init_app(app)
    jinja_filters.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True, load_dotenv=True)