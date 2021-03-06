import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    # Docker?
    DOCKER = os.environ.get('DOCKER') or False
    # TED Endpoint
    HOST = os.environ.get('HOST') or "demo.theenergydetective.com"
    HOSTPORT = os.environ.get('HOSTPORT') or '80'
    # Util Info
    COST = os.environ.get('COST') or '0'
    TAX = os.environ.get('TAX') or '0'
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
    VERSION = '1.5'
    DBVER = '1.0'


class TestingConfig():
    # Set for testing
    TESTING = True
    DBHOST = os.environ.get('DBHOST') or '127.0.0.1'
    DBPORT = os.environ.get('DBPORT') or '5432'
    DBUSER = os.environ.get('DBUSER') or 'pyted'
    DBPASS = os.environ.get('DBPASS') or 'password'
    DOCKER = True
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
    # version
    VERSION = '0.0.0'
    DBVER = '0.0'
