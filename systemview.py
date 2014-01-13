# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
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

    # render the search template and send it the hostname we found
    return render_template('proc_search.html', hostname=hostname)


@app.route('/procs/', methods=['POST'])
def show_procs():
    # this method gets the system processes matching the search term

    # let's get the host name of this vm to display on the page
    hostname = get_hostname()

    # first, get the search term out of the POST data
    term = request.form['term']

    # now lets get all the system processes
    raw_procs = subprocess.Popen(['ps', 'aux'],
                                 stdout=subprocess.PIPE).communicate()[0]

    # now filter the raw process list to find lines with our term
    count = 0
    procs = []
    for line in raw_procs.split("\n"):
        # If the correct name was found, show it and increment count
        if term in line:
            procs.append(line)
            count += 1

    # render the search template, this time with our data
    return render_template('proc_search.html',
                           procs=procs, count=count, hostname=hostname)


# this method doesn't have a decorator, it's just a utility method
def get_hostname():
    # use the subprocess module to get the hostname
    # if there is some error, just use a default
    try:
        hostname = subprocess.Popen('hostname',
                                    stdout=subprocess.PIPE).communicate()[0]
    except CalledProcessError:
        hostname = "Unknown"

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
