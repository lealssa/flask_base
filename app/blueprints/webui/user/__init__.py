from flask import Blueprint

from blueprints.webui.user.views import login, logout, register, recover_user, reset_password

bp_user = Blueprint("user", __name__, template_folder="templates", url_prefix='/user')

bp_user.add_url_rule("/login", view_func=login, endpoint="login", methods=['POST', 'GET'])
bp_user.add_url_rule("/logout", view_func=logout, endpoint="logout", methods=['GET'])
bp_user.add_url_rule("/register", view_func=register, endpoint="register", methods=['POST', 'GET'])
bp_user.add_url_rule("/recover", view_func=recover_user, endpoint="recover", methods=['POST', 'GET'])
bp_user.add_url_rule("/reset", view_func=reset_password, endpoint="reset", methods=['POST', 'GET'])