systemview
==========

Example webapp project for the OSL DevOps Bootcamp

This is a small application using the Flask framework.

Installation
------------

Do this in your VM! To get into your VM, use `vagrant ssh` in the correct repo.

```
$ cd
$ sudo yum -y install python-virtualenv* # Installs the program virtualenv
$ virtualenv ~/systemview_venv # create a new virtualenv in your home directory
$ source ~/systemview_venv/bin/activate # activate the virtualenv
$ git clone git@github.com:DevOpsBootcamp/systemview.git # clone the code
$ cd systemview # enter the application's directory
$ pip install -r requirements.txt # install the packages systemview needs
``` 

Using the app
-------------

Once everything is installed and the database is set up correctly:

```
$ source ~/systemview_venv/bin/activate # enter the virtual environment
$ cd ~/systemview
$ git branch                          # check that you're on the correct branch
$ python systemview.py -i 0.0.0.0 -d # start the webapp
# in your web browser, go to 0.0.0.0:5050
``` 
