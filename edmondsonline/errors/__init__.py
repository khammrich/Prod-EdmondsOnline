from flask import Blueprint

bp = Blueprint('errors', __name__)

from edmondsonline.errors import handlers
