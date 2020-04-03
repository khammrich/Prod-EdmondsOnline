from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from guess_language import guess_language
from edmondsonline import db
from edmondsonline.main.forms import EditProfileForm, PostForm
from edmondsonline.models import User, Post
from edmondsonline.translate import translate
from edmondsonline.main import bp
from edmondsonline.landing import bp

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/landing', methods=['GET', 'POST'])
def landing():
    return render_template(
        'landing/landing.html')
        
        
@bp.route('/poems', methods=['GET', 'POST'])
def poems():
    return render_template(
        'landing/poems.html',
        title=_('Poems'))
        
        
@bp.route('/articles', methods=['GET', 'POST'])
def articles():
    return render_template(
        'landing/articles.html',
        title=_('Articles'))
        
        
@bp.route('/so_here_we_are', methods=['GET', 'POST'])
def art1():
    return render_template(
        'articles/art1.html',
        title=_('So Here We Are'))


@bp.route('/poor_cats', methods=['GET', 'POST'])
def art2():
    return render_template(
        'articles/art2.html',
        title=_('Poor Cats'))


@bp.route('/graphs', methods=['GET', 'POST'])
def graphs():
    return render_template(
        'articles/graphs.html',
        title=_('Graphs'))
        

@bp.route('/resources', methods=['GET', 'POST'])
def resources():
    return render_template(
        'articles/resources.html',
        title=_('Resources'))


@bp.route('/iframe', methods=['GET', 'POST'])
def iframetest():
    return render_template(
        'articles/iframetest.html',
        title=_('iframetest'))