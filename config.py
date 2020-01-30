import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    # TED Endpoint
    HOST = os.environ.get('HOST')
    # Util Info
    COST = os.environ.get('COST') or '0'
    METERREAD = os.environ.get('METERREAD') or '1'
    # Weather station
    PWS = os.environ.get('PWS') or 'KCALONGB124'
    # TimeZone
    TZ = os.environ.get('TZ') or 'UTC'
    # Database
    DBHOST = os.environ.get('DBHOST') or '127.0.0.1'
    DBPORT = os.environ.get('DBPORT') or '5432'
    DBUSER = os.environ.get('DBUSER')
    DBPASS = os.environ.get('DBPASS')
    DBDB = os.environ.get('DBDB') or 'pyted'
    # Mail Server
    MAIL_SERVER = os.environ.get('MAILHOST') or '127.0.0.1'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # Admins
    ADMINS = ['noreply@null.com']
    # available languages
    LANGUAGES = {
        'en': 'English'
    }
    # version
    VERSION = '0.0.3'
    DBVER = '0.3'
