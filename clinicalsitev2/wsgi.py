"""
WSGI config for clinicalsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from os.path import join,dirname,abspath
import sys
from django.core.wsgi import get_wsgi_application

# Add this file path to sys.path in order to import settings
PROJECT_DIR = dirname(dirname(abspath(__file__)))

#os.environ["DJANGO_SETTINGS_MODULE"] = "clinicalsite.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clinicalsitev2.settings")

DEBUG = True

application = get_wsgi_application()
