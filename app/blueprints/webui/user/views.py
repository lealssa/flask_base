from operator import ne
from flask import render_template, request, flash, redirect, url_for, abort
from flask_login import login_required, logout_user, current_user, login_user
from pydantic.error_wrappers import ValidationError

from models.error import (
    UsernameOrPasswordInvalidError, 
    UserNotFoundError,
    IvalidPasswordResetTokenError,
    UserExistsError
)

from models.user import (
    UserLoginViewModel,
    UserRegistrationViewModel,
    UserEmailRecoverViewModel,
    UserPasswordResetViewModel
)

from domain.user import UserDomain

from services.security import is_safe_url

def login():

    if current_user.is_authenticated:
        return redirect(url_for('webui.index'))

    if request.method == 'POST':            
        try:
            user_login = UserLoginViewModel(**request.form)

            user_to_login = UserDomain.ValidateUserCredentials(user_login)
            login_user(user_to_login)

            next = request.args.get('next')
            # is_safe_url should check if the url is safe for redirects.
            # See http://flask.pocoo.org/snippets/62/ for an example.
            if not is_safe_url(next):
                return abort(400)

            return redirect(next or url_for('webui.index'))            
        except ValidationError as e:
            print(e)
            flash('Verifique os campos e tente novamente','is-danger')
        except (UsernameOrPasswordInvalidError, UserNotFoundError):
            flash('Usuário ou senha inválidos', 'is-danger')
            
    return render_template('user/login.html')    

@login_required
def logout():
    logout_user()
    return redirect(url_for('webui.user.login')) 

def register():
    
    if request.method == 'POST':   
        try:     
            user_register = UserRegistrationViewModel(**request.form)

            UserDomain.RegisterUser(user_register)

            return render_template('user/register.html', user_created=True)
        except ValidationError as e:
            print(e)
            flash('Verifique os campos e tente novamente','is-danger')
        except UserExistsError:
            return render_template('user/register.html', user_exists=True)
            
    return render_template('user/register.html')

def recover_user():
    
    if request.method == 'POST':   
        try:                 
            user_recover = UserEmailRecoverViewModel(**request.form)

            UserDomain.SendPasswordResetIdEmail(user_recover)

            return render_template('user/recover_user.html', email_was_send=True)   
        except ValidationError as e:
            print(e)
            flash('Endereço de email inválido','is-danger')
        except UserNotFoundError:
            return render_template('user/recover_user.html', user_not_found=True)                 
        
    return render_template('user/recover_user.html') 

def reset_password():

    reset_token = request.args.get('token')

    if not reset_token:
        return redirect(url_for('webui.user.login')) 
    
    if request.method == 'POST':   
        try:            
            user_reset_password = UserPasswordResetViewModel(**request.form)

            UserDomain.ResetUserPassword(user_reset_password)

            return render_template('user/reset_password.html', has_reset=True)               

        except ValidationError as e:
            print(e)
            flash('A senha precisa ter no mínimo 6 caracteres','is-danger')
        except IvalidPasswordResetTokenError:
            return render_template('user/reset_password.html', invalid_token=True)            
          
    return render_template('user/reset_password.html', reset_token=reset_token)         