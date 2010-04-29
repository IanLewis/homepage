import os
import sys

PYTHON_PATH = '/home/ianlewis/webapps/homepage/lib/python2.5'
VHOST_PATH = '/home/ianlewis/webapps/homepage'
VENV_PATH = '/var/www/venvs/sitebackstage'
SETTINGS_MOD = 'settings_production'

sys.path.insert(0, VHOST_PATH)
sys.path.insert(0, os.path.join(VHOST_PATH, 'hp'))
sys.path.insert(0, PYTHON_PATH)

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'hp.settings_local'
application = WSGIHandler()
