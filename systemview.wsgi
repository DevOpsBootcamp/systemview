activate_this = '/var/www/html/systemview/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/html/systemview')

from systemview import app as application
