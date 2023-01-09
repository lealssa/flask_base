from flask import Flask
from models.settings import Settings

app_settings = Settings()

def init_app(app: Flask):

    app.secret_key = app_settings.secret_key
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['FLASK_PYDANTIC_VALIDATION_ERROR_RAISE'] = True    
    app.config['USE_SESSION_FOR_NEXT'] = True