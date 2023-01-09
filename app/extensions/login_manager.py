from flask import Flask, request, abort, redirect, url_for, flash
from flask_login import LoginManager
from http import HTTPStatus

from repository.user import UserRepository
from models.user import UserBase, UserLogin

def init_app(app: Flask):

    login_manager = LoginManager()
    login_manager.init_app(app)   
    # login_manager.login_view = "webui.user.login"
    # login_manager.login_message = "Faça login para acessar a página"
    login_manager.session_protection = 'strong'
    login_manager.login_message_category = "is-danger"

    @login_manager.user_loader
    def load_user(user_id):      
        user_login = None  
        user_repo = UserRepository(UserBase).get_by_str(user_id).first()
        if user_repo:
            user_login = UserLogin(**user_repo.dict())

        return user_login

    @login_manager.unauthorized_handler
    def unauthorized():
        if request.path.startswith('/api/'):            
            abort(HTTPStatus.UNAUTHORIZED)
        flash('Faça login para acessar a página', 'is-danger')
        return redirect(url_for('webui.user.login', next=request.path))        

