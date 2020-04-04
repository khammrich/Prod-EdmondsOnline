from flask import Blueprint

bp = Blueprint('main', __name__)

from edmondsonline.main import routes
