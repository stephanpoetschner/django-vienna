# Django Fixtures

* *speaker* Florian Demmer
* Django-Freelancer
* http://floriandemmer.com/
* Github: https://github.com/fdemmer
* *slides*: http://slides.com/fdemmer/django-friends_2014-03-25/

https://docs.djangoproject.com/en/dev/howto/initial-data/#providing-initial-data-with-fixtures

## Notes

* avoid initialization of `init_data.*`: `manage.py syncdb --no-initial-data` (new in 1.5)
* Django 1.7 will [not load fixtures](https://docs.djangoproject.com/en/dev/releases/1.7/)
  from apps with existing migrations.
* Better dumpdata: `manage.py dumpdata --indent 4 --natural`

## Questions & Answers

* Alternatives to Fixtures?
    * [Factory Boy](http://factoryboy.readthedocs.org/)
    * [django_extensions](http://django-extensions.readthedocs.org/) (`manage.py dumpscript` and `manage.py runscript`)
* How do you deal with tests and fixtures?
  It is important to keep the data-set in fixtures small and well maintained –
  making changes in the model less painless.
* How do you handle files referenced in fixtures?
  Just put them into your static-folder and reference them via relative paths.