oksicat
=======

Dependencies
============

    - python 2.7.3
    - django 1.4.5
    - django-admin-tools 0.5.1
    - south 0.7.6

Install
=======

	virtualenv .
	source bin/activate
	pip install -r reqs.txt
	./manage.py syncdb
	./manage.py migrate

Use
===
	source bin/activate
	./manage.py runserver
