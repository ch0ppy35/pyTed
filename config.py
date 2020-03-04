import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    # Docker?
    DOCKER = os.environ.get('DOCKER') or False
    # TED Endpoint
    HOST = os.environ.get('HOST') or "demo.theenergydetective.com"
    # Util Info
    COST = os.environ.get('COST') or '0'
    METERREAD = os.environ.get('METERREAD') or '1'
    # Weather station
    PWS = os.environ.get('PWS') or 'KDEN'
    # TimeZone
    TZ = os.environ.get('TZ') or 'America/Denver'
    # Database
    DBHOST = os.environ.get('DBHOST') or '127.0.0.1'
    DBPORT = os.environ.get('DBPORT') or '5432'
    DBUSER = os.environ.get('DBUSER') or 'pyted'
    DBPASS = os.environ.get('DBPASS') or 'password'
    DBDB = os.environ.get('DBDB') or 'pyted'
    # available languages
    LANGUAGES = {
        'en': 'English'
    }
    # version
    VERSION = '1.0-RC1'
    DBVER = '1.0'


class TestingConfig():
    # Set for testing
    TESTING = True
    DBHOST = os.environ.get('DBHOST') or '127.0.0.1'
    DBPORT = os.environ.get('DBPORT') or '5432'
    DBUSER = os.environ.get('DBUSER')
    DBPASS = os.environ.get('DBPASS')
    # Demo Ted Address
    HOST = "demo.theenergydetective.com"
    FLASK_APP = "pyTED.py"
    # Util Info
    COST = os.environ.get('COST') or '0'
    METERREAD = os.environ.get('METERREAD') or '1'
    # Weather station
    PWS = os.environ.get('PWS') or 'KCALONGB124'
    # TimeZone
    TZ = os.environ.get('TZ') or 'America/Denver'
    # Database
    DBDB = os.environ.get('DBDB') or 'pyted'
    # Mail Server
    MAIL_SERVER = os.environ.get('MAILHOST') or '127.0.0.1'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # version
    VERSION = '0.0.0'
    DBVER = '0.0'
