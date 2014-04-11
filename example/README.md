django-buildout-sample
======================

* Work in progress sample repository to illustrate usage of buildout/gunicorn/supervisor/nginx with a Django project.

Setup
-----

Create a PROJECT_DIR and clone git repository.

    $> mkdir <PROJECT_DIR>
    $> cd <PROJECT_DIR>
    $> git clone https://github.com/muuux/django-buildout-sample.git .

Create virtualenv, run bootstrap and buildout.

    $> virtualenv .
    $> bin/python bootstrap.py
    $> bin/buildout

Run django syncdb and collectstatic.

    $> bin/django syncdb
    $> bin/django collectstatic

Start supervisord (starts gunicorn service) and nginx.

    $> bin/supervisord
    $> bin/nginxctl start

Check if gunicorn started.

    $> bin/supervisorctl status

If everything went well the django project should be available at ``127.0.0.1:8088/admin/``
