from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user, login_required
from blueprints.webui.user import bp_user

bp = Blueprint("webui", __name__, template_folder='templates', url_prefix='/')
bp.register_blueprint(bp_user)

@login_required
def index():
    return render_template('index.html') 

def page_not_found(exception):
    if request.path.startswith('/api/'):
        return jsonify(error='not found'), 404   
    else:        
        return render_template('404.html')

bp.add_url_rule("/", view_func=index, endpoint="index", methods=['POST', 'GET'])    

def init_app(app):
    app.register_blueprint(bp)
    app.register_error_handler(404, page_not_found)