# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
import collections
import os
# import json
import simplejson as json
from flask import Flask, render_template, request, flash, url_for, Response
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_login import LoginManager, login_user, login_required, current_user
from werkzeug.utils import redirect
# import models
from models import User, Campaigns, engine, CampaignDetails, Stations
from forms import *

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''


# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        campaign = Campaigns(current_user.user_id, request.form['product'], request.form['campaign_name'])
        db.session.add(campaign)
        db.session.commit()
        flash('Campaign successfully registered')
        return redirect(url_for('index'))
    form = NewCampaignForm(request.form)
    return render_template('user_pages/index.html', form=form)



@app.route('/getadverts')
@login_required
def getadverts():
    i = 1
    connection = engine.connect()
    rs = connection.execute("select campaign_id, product, campaign_name,"
                            + "SUM(CASE WHEN (station_type_desc='Local Station') THEN 1 ELSE 0 END) AS LocalStation, "
                            + "SUM(CASE WHEN (station_type_desc='Radio') THEN 1 ELSE 0 END) AS Radio "
                            + "from ( "
                            + "select cmp.campaign_id, product, campaign_name, station_name, station_type_desc "
                            + "from medmo.campaigns cmp left join medmo.campaigndetails cmpd ON cmp.campaign_id = cmpd.campaign_id "
                            + "left join medmo.stations stn ON cmpd.station_id = stn.station_id "
                            + "left join medmo.stationtypes stntp ON stn.station_type_id = stntp.station_type_id "
                            + "where cmp.createdby_user_id = " + str(current_user.user_id)
                            + ") as summary group by product, campaign_name order by campaign_id desc;")
    pyadverts = []
    for row in rs:
        if i % 2 == 1:
            style = 'oddcard'
        else:
            style = 'evencard'
        # print row
        d = collections.OrderedDict()
        d['id'] = row.campaign_id
        d['product'] = row.product
        d['campaign'] = row.campaign_name
        d['tvStations'] = row.LocalStation
        d['radioStations'] = row.Radio
        d['style'] = style
        pyadverts.append(d)
        i += 1
    return Response(json.dumps(pyadverts), mimetype='application/json', headers={'Cache-Control': 'no-cache'})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm(request.form)
        return render_template('forms/login.html', form=form)
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username, password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    # return render_template('pages/placeholder.about.html')
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm(request.form)
        return render_template('forms/register.html', form=form)
    user = User(request.form['username'], request.form['password'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))


@app.route('/getadvertdetails')
@login_required
def getadvertdetails():
    advert_id = request.args['a']
    connection = engine.connect()
    i = 0
    rs = connection.execute("SELECT cmpd.campaign_id, cmpd.station_id, station_name, station_type_desc, stn.station_type_id, "
                            + "schedule_dates FROM medmo.campaigndetails cmpd join medmo.stations stn ON "
                            + "cmpd.station_id = stn.station_id join medmo.stationtypes stntp ON "
                            + "stn.station_type_id = stntp.station_type_id WHERE cmpd.campaign_id = " + str(advert_id)
                            + " ORDER BY station_type_id, station_id;")
    advertdetails = []
    for row in rs:
        if i % 2 == 1:
            style = 'oddcard'
        else:
            style = 'evencard'
        d = collections.OrderedDict()
        d['campaign_id'] = row.campaign_id
        d['station_id'] = row.station_id
        d['station_name'] = row.station_name
        d['station_type_desc'] = row.station_type_desc
        d['station_type_id'] = row.station_type_id
        d['schedule_dates'] = row.schedule_dates
        d['style'] = style
        advertdetails.append(d)
    return Response(json.dumps(advertdetails), mimetype='application/json', headers={'Cache-Control': 'no-cache'})


@app.route('/editadvert', methods=['GET', 'POST'])
@login_required
def editadvert():
    if request.method == 'POST':
        campaign_id = request.form['campaign_id']
        station_id = request.form['station_id']
        schedule_dates = request.form['schedule_dates']
        # campaigndtls = CampaignDetails(campaign_id, station_id, schedule_dates)
        # db.session.update(campaigndtls)
        # db.session.commit()
        update_advert = db.session.query(CampaignDetails).filter_by(campaign_id=campaign_id, station_id=station_id).update({CampaignDetails.schedule_dates:schedule_dates})
        db.session.commit()
        db.session.flush()
        if update_advert > 0:
            flash('Campaign successfully edited')
        else:
            flash('Cannot edited campaign')
        return redirect(url_for('editadvert')+'?'+request.form['campaign_id'])
    editForm = EditCampaignDetail(request.form)
    addForm = AddCampaignDetail(request.form)
    addForm.add_station_id.choices = [(g.station_id, g.station_name) for g in Stations.query.order_by('station_id')]
    return render_template('user_pages/editadvert.html', editForm=editForm, addForm=addForm, advertid=request.query_string)


@app.route('/addnewschedule', methods=['GET', 'POST'])
def addnewschedule():
    if request.method == 'POST':
        campaign_id = request.form['add_campaign_id']
        station_id = request.form['add_station_id']
        schedule_dates = request.form['add_schedule_dates']
        campaigndtls = CampaignDetails(campaign_id, station_id, schedule_dates)
        db.session.add(campaigndtls)
        db.session.commit()
        db.session.flush()
        return redirect(url_for('editadvert')+'?'+request.form['add_campaign_id'])


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)


# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    # db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

# Default port:
'''
if __name__ == '__main__':
    app.run()
'''

# Or specify port manually:

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
