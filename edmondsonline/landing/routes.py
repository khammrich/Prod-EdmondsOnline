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
def vbart1():
    return render_template(
        'articles/vbart1.html',
        title=_('So Here We Are'))


@bp.route('/covidWiki', methods=['GET', 'POST'])
def wiki():
    return render_template(
        'articles/wiki.html',
        title=_('Poor Cats'))


@bp.route('/selfchecker', methods=['GET', 'POST'])
def selfchecker():
    return render_template(
        'articles/selfchecker.html',
        title=_('Poor Cats'))

@bp.route('/whoupdates', methods=['GET', 'POST'])
def whoupdates():
    return render_template(
        'articles/whoupdates.html',
        title=_('WHO Updates'))