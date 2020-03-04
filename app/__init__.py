from flask import Flask
import logging
import os
from logging.handlers import RotatingFileHandler, SMTPHandler
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

if not os.path.exists('logs'):
    os.mkdir('logs')

# Normal logging setup
file_handler = RotatingFileHandler('logs/pyted.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

import setup

setup.dbCheck()

app.logger.info('~ pyTed is starting up ~')

from app import routes, errors
from app.chores import cronTasks, tasks, queries, scheduledTasks
from app.tools import database
