from flask import Flask
import logging
import os
from logging.handlers import RotatingFileHandler, SMTPHandler
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

if not os.path.exists('logs'):
    os.mkdir('logs')

# Normal logging
file_handler = RotatingFileHandler('logs/pyted.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)

# Mail logging on errors (Needs work)
if not app.debug and app.config['MAIL_SERVER'] != '':
    credentials = None
    app.logger.info('~ Trying to turn on mail services ~')
    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
        credentials = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    mail_handler = SMTPHandler((app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                               'no-reply@' + app.config['MAIL_SERVER'], app.config['ADMINS'], 'pyTed failure',
                               credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
else:
    app.logger.info('~ Not turning on mail services ~')

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('~ pyTed is starting up ~')

from app import routes, database, errors
