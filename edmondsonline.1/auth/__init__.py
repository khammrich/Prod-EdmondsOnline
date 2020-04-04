from flask import Blueprint

bp = Blueprint('auth', __name__)

from edmondsonline.auth import routes
