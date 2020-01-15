from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/pyted.log', maxBytes=10240,
                                   backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('pyTed startup')

from app import routes
