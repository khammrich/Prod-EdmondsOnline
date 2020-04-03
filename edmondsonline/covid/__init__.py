from flask import Blueprint

bp = Blueprint('covid', __name__)

from edmondsonline.covid import routes
