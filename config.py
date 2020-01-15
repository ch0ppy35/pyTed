import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = os.environ.get('HOST')
    DBHOST = os.environ.get('DBHOST')
    DBPORT = os.environ.get('DBPORT')
    DBUSER = os.environ.get('DBUSER')
    DBPASS = os.environ.get('DBPASS') or 'oh-yeah'