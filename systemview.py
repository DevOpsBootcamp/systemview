# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
import subprocess
import sys
import argparse

# this is a single line comment

"""
This is a multiline comment.
It is good for long descriptions of stuff.
    * good way to outline what you are trying to do before writing code
    * can add docstrings here that can be used to generate documentation
    * don't forget to close with three double-quotes
"""

# create the application
app = Flask(__name__)

# tell the app where our db is.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vagrant:password@localhost/systemview'

# set up the db through SQLAlchemy
db = SQLAlchemy(app)
db.init_app(app)


# declare our Search model to hold previous search terms.
class Search(db.Model):
    # tell the model what to name the table
    __tablename__ = 'searches'

    # this is where we declare the types of our database columns
    # and relationships between tables
    term = db.Column(db.String(100), primary_key=True)

    # this defines what to do, and which parameters to provide when
    # creating a Search object.
    def __init__(self, term):
        self.term = term


"""
@app.route is a decorator - it tells the app what URL to respond to
with this method. This method will be run when someone goes to
http://your_app_address/
"""


@app.route('/')
def show_form():
    # this method will show a form asking for a search string

    # first, let's get the host name of this vm to display on the form
    hostname = get_hostname()

    # Now let's get all the previous searches
    searches = Search.query.all()

    # render the search template and send it the hostname we found
    return render_template('proc_search.html', hostname=hostname,
                            searches=searches)


@app.route('/procs/', methods=['POST'])
def show_procs(term=None):
    # this method gets the system processes matching the search term

    # let's get the host name of this vm to display on the page
    hostname = get_hostname()

    # get the search term out of the POST data
    term = request.form['term']

    # now lets get all the system processes
    raw_procs = subprocess.Popen(['ps', 'auxh'],
                                 stdout=subprocess.PIPE).communicate()[0]

    # now filter the raw process list to find lines with our term
    count = 0
    procs = []
    for line in raw_procs.split("\n"):
        # If the correct name was found, show it and increment count
        if term in line:
            procs.append(line)
            count += 1

    # check to see if the term is already in the db
    search = Search.query.filter_by(term=term).first()

    # check to see that we entered a term, and it's not in the db
    if term and not search:

        # create an object from our search term
        search = Search(term)

        # add and commit it to the db
        db.session.add(search)
        db.session.commit()

    searches = Search.query.all()

    # render the search template, this time with our data
    return render_template('proc_search.html', searches=searches,
                           procs=procs, count=count, hostname=hostname)


# this method doesn't have a decorator, it's just a utility method
def get_hostname():
    # use the subprocess module to get the hostname
    # if there is some error, just use a default
    hostname = "Unknown"
    try:
        hostname = subprocess.Popen(['hostname'],
                                    stdout=subprocess.PIPE).communicate()[0]
    except:
        pass

    # subprocess returns a hostname with a newline (\n) - lets remove it
    return hostname.rstrip()


# this starts the application up if you run it from the
# command line
if __name__ == '__main__':

    sys.dont_write_bytecode = True

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", help="listen to this IP address",
                        default="127.0.0.1")
    parser.add_argument("-p", "--port", help="listen to this port",
                        default="5000", type=int)
    parser.add_argument("-d", "--debug", help="turn debugging on",
                        action="store_true")

    args = parser.parse_args()

    app.run(args.ip, args.port, args.debug)
