INSTALL
-------
- Install python 2.7.x
- Install MySQL
- Install PIP
- sudo pip install virtualenv
- cd to workspace
- virtualenv env
- source ./env/bin/activate
- git clone git@github.com:openeyes/cnd.git
- cd cnd
- pip install -r requirements.txt
- ./manage.py migrate
- ./manage.py loaddata initial_data
- ./manage.py createsuperuser
- ./manage.py runserver
- configure site setting through web admin

