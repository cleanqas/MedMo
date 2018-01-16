from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from datetime import datetime
# from app import db
# import app

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"

# engine = create_engine('sqlite:///database.db', echo=True)
engine = create_engine(DB_URI.format(
                                  user ='root',
                                  password = 'oracle',
                                  host = 'localhost',
                                  port = '3306',
                                  db = 'medmo'),
                          connect_args = {'time_zone': '+00:00'},
                          echo=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Set your classes here.


class User(Base):
    __tablename__ = 'Users'

    user_id = Column('user_id', Integer, primary_key=True)
    username = Column('username', String(120), unique=True,
                         index=True)
    email = Column('email', String(120), unique=True,
                      index=True)
    password = Column('password', String(30))
    company_id = Column('company_id', Integer, index=True)
    registered_on = Column('registered_on', DateTime)

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.user_id)

    def __repr__(self):
        return '<User %r>' % (self.username)


class Companies(Base):
    __tablename__ = 'Companies'
    company_id = Column('company_id', Integer, primary_key=True)
    company_name = Column('company_name', String(120))
    company_address = Column('company_address', String(120))

    def __repr__(self):
        return '<Company: %r>' % (self.company_name)


class Stations(Base):
    __tablename__ = 'Stations'
    station_id = Column('station_id', Integer, primary_key=True)
    station_name = Column('station_name', String(120))
    station_type_id = Column('station_type_id', Integer, index=True)


class StationTypes(Base):
    __tablename__ = 'StationTypes'
    station_type_id = Column('station_type_id', Integer, primary_key=True)
    station_type_desc = Column('station_type_desc', String(120))


class Campaigns(Base):
    __tablename__ = 'Campaigns'
    campaign_id = Column('campaign_id', Integer, primary_key=True)
    createdby_user_id = Column('createdby_user_id', Integer, index=True)
    product = Column('product', String(120), index=True)
    campaign_name = Column('campaign_name', String(120))

    def __init__(self, createdby_user_id=None, product=None, campaign_name=None):
        self.createdby_user_id = createdby_user_id
        self.product = product
        self.campaign_name = campaign_name

    def __repr__(self):
        return '<Campaign: %r>' % (self.campaign_name)


class CampaignDetails(Base):
    __tablename__ = "CampaignDetails"
    id = Column('id', Integer, primary_key=True)
    campaign_id = Column('campaign_id', Integer, index=True)
    station_id = Column('station_id', Integer, index=True)
    schedule_dates = Column('schedule_dates', String(750))

    def __init__(self, campaign_id=None, station_id=None, schedule_dates=None):
        self.campaign_id = campaign_id
        self.station_id = station_id
        self.schedule_dates = schedule_dates

    def __repr__(self):
        return '<Campaign Dates: %r>' % (self.schedule_dates)

# Create tables.
Base.metadata.create_all(bind=engine)
