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
from edmondsonline.covid import bp


@bp.route('/graphs', methods=['GET', 'POST'])
def graphs():
    return render_template(
        'coviddata/graphs.html',
        title=_('Graphs'))
        

@bp.route('/resources', methods=['GET', 'POST'])
def resources():
    return render_template(
        'coviddata/resources.html',
        title=_('Resources'))


@bp.route('/WA_State_Map', methods=['GET', 'POST'])
def wastate():
    return render_template(
        'coviddata/cov19wamap.html',
        title=_('WA State COVID-19 Map'))
        
        
@bp.route('/Covid_FAQ', methods=['GET', 'POST'])
def covidfaq():
    return render_template(
        'coviddata/covidfaq.html',
        title=_('Covid_FAQ'))


@bp.route('/WHO_Interactive_Map', methods=['GET', 'POST'])
def whoworld():
    return render_template(
        'coviddata/whoworld.html',
        title=_('Covid_FAQ'))