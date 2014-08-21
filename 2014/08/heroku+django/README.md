# Heroku & Django: Lessons Learned

* *speaker* Stephan Pötschner
* Django-Freelancer
* http://stephan-poetschner.at/
* Github: https://github.com/stephanpoetschner
* *slides*: https://docs.google.com/presentation/d/1DDm--PmzRRfH_LLmngb5WMDu7rQpgK7Z27mQPQnEcsU/edit?usp=sharing

# Notes

## Django & Heroku – Hosting your project on Heroku

Talking about my last project (microsite for big e-commerce site with lots of traffic and marketing budget).


### Takeaways (1 / 3)

You feel great when it works.
Heroku is a great platform with it's biggest advantage being (almost) seamless scalability.

Our App:
* Average Response-Time: 190ms (10. Juli 2014).
* Dynamic Scaling of dynos (>100 parallel user and 45.000 requests/hour).
    * 70.000 visitors within a day.

Image: http://flic.kr/p/fq2i4C

### Takeaways (2 / 3)

Expensive to make it work properly (in terms of cash and learning curve).
More details later.

Image: http://flic.kr/p/nSpCNu

### Takeaways (3 / 3)

YOU WILL NOT NEED IT!
Except for big-clients with indeterminate traffic spikes.

AS said: Heroku's main advantage is scalability. But in most of my projects, you will not need this 
additional flexibility and therefore will be far more efficient using your traditional hosting.

It is not better or worse than traditional hosting, it is a different use case.

My Project-Setup: 
* Big german Consumer-E-Commerce site going live. 
* One of several microsites. 
* Microsite was actively promoted by prominent Facebook users (https://www.facebook.com/pages/Anne-Menden/146681832060471 500k fans).
* Client Traffic Estimations for Launch: 100 parallel users

Image: http://flic.kr/p/npPh5b

### Heroku is great (1 / 3)
APPS, APPS, APPS

You can buy lot of high quality functionality by adding heroku apps.

* Postgres (50$)
   * postgres-plans (https://devcenter.heroku.com/articles/heroku-postgres-plans#standard-tier)
   * Update on plans at beginning of august 2014
* Postgres Backups (0$)
* Logentries (45$, backups to S3)
* Adapt Scale (18$, ø4 dynos)
* Memcachier (15$, 100mb)
* Sendgrid (0$)

Optional:
* Searchbox ElasticSearch (9$)
* CloudAMQP (19$)

You will save money for wages, since setting up apps is just a matter of clicking stuff in the interface.
You will have to pay more money for running the functionality compared to baking the infrastructure on your own environment.

Image: http://flic.kr/p/nzNQmK

### Heroku is great (2 / 3)

Toolbelt

Install Heroku Toolbelt on your local machine.

Start a new worker and run a python shell in your application environment.
(NOTE: You will not connect to one of your web-workers!).

    $ heroku run 'python manage.py shell_plus'


Set your application to debug-mode (by changing it's environment variable).

    $ heroku config:set DEBUG=True

It's easy to access your heroku-database from commandline.

    $ heroku pgbackups:url --app myproject
    $ heroku pg:reset DATABASE_URL --app myproject-dev
    
Image: http://flic.kr/p/nCqyra

### Heroku is great (3 / 3)

* Good Documentation
    * https://devcenter.heroku.com/articles/getting-started-with-python
    * https://devcenter.heroku.com/articles/getting-started-with-django


Image: http://flic.kr/p/dQm85A

### Heroku is Expensive (1 / 4)

APPS are expensive.
128$ for MY minimum setup. (see slide "APPS, APPS, APPS")

Image: http://flic.kr/p/8Drov3

### Heroku is Expensive (2 / 4)
Dynos are expensive. 
Run 2 Dynos: 34$ 
(1 is free. Sleeps – if idle)

> Rule of thumb:
> 1 heroku-dyno -> 3 gunicorn workers.

**Compared to traditional hosting:**

* Webfaction: ~10USD runnning 12 gunicorn-workers.
* Heroku: 12 gunicorn-workers: ~100USD

Image: http://flic.kr/p/7mzTCa

### Heroku is Expensive (3 / 4)

* Bad Performance.
    * Laptop vs. Heroku vs. Bare-Metal Server (traditional hosting)
    * Lots of caching. [1]

[1] Asynchronously preparing JSON Responses as good as possible (additional workers):
* products task (most dynamic): cache for 5 minutes, update every 10 secs, exclude sensitive information (pricing, availability)
* facets task, idols task, outfits task, shots task, socials task
* dynamically add likes, comments


Image: http://flic.kr/p/hUBNdK

### Heroku is Expensive (4 / 4)

It's a Cloud Environment – it's a special Environment
* Upload media files to cloud [1]
* No dirty-fixes via SSH [2]
* Settings via Environment [3]
* Customizing your build is hard [4].
* Heroku-Patches (pylibmc) [5]
* No Cronjobs (worker or celery)

---

[1] 

    $ pip install django-storages==1.1.8

`settings.py`

    DEFAULT_FILE_STORAGE = env.config('storages.backends.s3boto.S3BotoStorage’, '')
    STATICFILES_STORAGE = env.config('storages.backends.s3boto.S3BotoStorage', '')
    
    AWS_ACCESS_KEY_ID = env.config('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = env.config('AWS_SECRET_ACCESS_KEY', '')
    AWS_STORAGE_BUCKET_NAME = env.config('AWS_STORAGE_BUCKET_NAME', '')
    
    AWS_QUERYSTRING_AUTH = False
    AWS_QUERYSTRING_EXPIRE = 0
    AWS_PRELOAD_METADATA = True  # increases upload time of static-files

[2]

    $ heroku run 'bash' starts an additional worker.


[3]

    $ pip install django-toolbelt==0.0.1
    $ pip install dj-database-url==0.3.0
    $ pip install django-pylibmc-sasl==0.2.4
    
    $ heroku config
    MYPROJECT_DEBUG: True

`settings.py`

    from myproject.envsettings import Env
    env = Env('MYPROJECT')
    DEBUG = bool(env.config('DEBUG', False))

`envsettings.py`

    # coding: utf-8
    import os
    
    class Env(object):
        def __init__(self, app_name):
            self.app_name = app_name.upper()
    
        def config(self, setting, default):
            name = u'_'.join([self.app_name, setting, ])
            return os.environ.get(name, default)
    
        def raw(self, setting, default):
            return os.environ.get(setting, default)

[4]
buildpacks
* [app.json[(https://blog.heroku.com/archives/2014/5/22/introducing_the_app_json_application_manifest)
* [Deploy Buttons](https://devcenter.heroku.com/articles/heroku-button) (update beginning of august)

[5]

    CACHES = {
        'default': {
            'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
            'TIMEOUT': 1000,
            'BINARY': True,
            'OPTIONS': {
                'tcp_nodelay': True,
                'remove_failed': 4
            }
        }
    }


Image: http://flic.kr/p/fpL2y2

### Still want to deploy to Heroku? (1 / 2)

Have the right project/client 

and calculate your costs 
(development costs + ongoing infrastructure costs).

Image: http://www.flickr.com/photos/statelibraryofnsw/6433918107/

### Still want to deploy to Heroku? (2 / 2)

> Rule of Thumb:

> Use Heroku,
> when marketing budget hits your project.

(e.g. short lived marketing campaign)

Image: http://flic.kr/p/bDHEiy

### Thanks!

stephan.poetschner@gmail.com
stephan-poetschner.at
github.com/stephanpoetschner


Django Freelancer


## Q&A

### Alternatives to Heroku?

* [JiffyBox](http://www.df.eu/de/cloud-hosting/cloud-server/) – German Provider

More Low-Level
* Amazon EC2
* Google Compute Engine

### Do I have to run Postgres on one of my Dynos?

No, you just get an URL where you can connect to. Heroku will host you postgres instance.

### How to integrate with apps?

If the app has an API, it will typically set an environment variable. 
You will read and use the url from the environment variable in your django application.

If the app just provides an interface, you will get a link in your dashboard (e.g. logentries-application).
