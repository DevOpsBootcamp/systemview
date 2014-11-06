systemview
==========

Example webapp project for the OSL DevOps Bootcamp

This is a small application using the Flask framework.

Installation
------------

Do this in your VM! To get into your VM, use `vagrant ssh` in the correct repo.

```
$ cd

# Installs the program virtualenv
$ sudo yum -y install python-virtualenv* 

#Create a new virtual environment called 'systemview_venv'
$ virtualenv ~/systemview_venv

#Activate the virtualenv, or "turn it on".  This will put you inside of the virtualenv
$ source ~/systemview_venv/bin/activate

#Clone the repository
$ git clone git@github.com:DevOpsBootcamp/systemview.git 

#Go to the applications directory
$ cd systemview

#Install the packages that systemview needs.  The magically file requirements.txt will tell 
#pip what packages are needed and have it download them. 
$ pip install -r requirements.txt

#Execute scripte to create database tables
$ python create_tables.py
``` 

Using the app
-------------

Once everything is installed and the database is set up correctly:

``` 
# enter the virtual environment
$ source ~/systemview_venv/bin/activate

#Change directories to the web application
$ cd ~/systemview

#Make sure that you are on the $x branch.  The branch you are on will have an asterisk next to it.
$ git branch                         

#Start the app!  
$ python systemview.py -i 0.0.0.0 -d # start the webapp
``` 

In your web browser, go to http://0.0.0.0:5000

What the above command does is tells python to execute the code in systemview.py.
The '-i' is a custom argument that we pass to the file, telling it to listen to the IP address 0.0.0.0
0.0.0.0 means `all ip addresses on the local machine <http://serverfault.com/questions/78048/whats-the-difference-between-ip-address-0-0-0-0-and-127-0-0-1>`
The '-d' is another custom argument to turn debugging on, so that if something breaks we can
figure out where it's breaking a little bit easier.

