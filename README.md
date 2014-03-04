systemview
==========

Example webapp project for the OSL DevOps Bootcamp

This is a small application using the Flask framework.

Installation
------------

Do this in your VM! To get into your VM, use `vagrant ssh` in the correct repo.

```
$ cd
$ sudo yum -y install python-virtualenv*
$ virtualenv ~/systemview_venv
$ source ~/systemview_venv/bin/activate
$ pip install flask
$ pip install argparse
$ git clone git@github.com:DevOpsBootcamp/systemview.git
$ deactivate
``` 

Setting up the database to use save-search
------------------------------------------

All of the database development has been done on the `save-search` branch. 

In your VM (your prompt will read `vagrant@...` rather than your usual
username), use the catch-up instructions from
https://github.com/DevOpsBootcamp/catch-up

Using the app
-------------

Once everything is installed and the database is set up correctly:

```
$ source ~/systemview_venv/bin/activate
$ cd ~/systemview
$ git branch                          # check that you're on the correct branch
$ sudo /sbin/service mysqld start     # can only connect to db if it's running
$ python systemview.py -i 0.0.0.0 -d
# in your web browser, go to 0.0.0.0:5050
``` 
