import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    HOST = os.environ.get('HOST')
    DBHOST = os.environ.get('DBHOST')
    DBPORT = os.environ.get('DBPORT')
    DBUSER = os.environ.get('DBUSER')
    DBPASS = os.environ.get('DBPASS')
    PWS = os.environ.get('PWS') or 'KCALONGB124'