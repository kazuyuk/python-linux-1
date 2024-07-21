from subprocess import STDOUT, check_call
import os
#check_call(['apt-get', 'update'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
check_call(['apt-get', 'install', '-y', 'libgl1'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
check_call(['apt-get', 'install', '-y', 'libglib2.0-0'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
#check_call(['apt-get', 'update'], stdout=open(os.devnull,'wb'), stderr=STDOUT)

import xgboost as xgb
from flask import Flask
from applicationinsights.flask.ext import AppInsights
app = Flask(__name__)
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = '413d7290-841f-4f30-96ac-9353c368cef1'
appinsights = AppInsights(app)

@app.route('/')
def hello_world():
    app.logger.info('Info log entry')
    app.logger.debug('Debug log entry')
    #app.logger.error('Error Entry')
    return 'Hello, World!'
