import os, sys
sys.path.append('/var/www/forms/')
os.environ.setdefault('PYTHON_EGG_CACHE', '/tmp/.python-eggs')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newforms.settings")
# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
