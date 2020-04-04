from flask import Blueprint

bp = Blueprint('landing', __name__)

from edmondsonline.landing import routes
