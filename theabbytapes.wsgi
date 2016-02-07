#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/The-Abby-Tapes/")

from app import app
application = app
application.secret_key = 'My super seceret key'
