# Deploying Django Apps using Docker 

* *speaker:* [Thomas Kremmel](http://www.simpleloop.com)
* Django Developer, Simpleloop.com 
* *slides*: http://www.slideshare.net/ThomasKremmel/deploy-django-apps-using-docker?qid=aabe39cc-9ab4-44d8-beec-130d3f058f11&v=qf1&b=&from_search=1 

## Notes

Thomas and his company simpleloop are using Docker to deploy the Django apps developed for their customers to a shared host. Docker is great for deploying multiple Django apps onto one host.

Docker containers should store all persistent data outside the container. So the log files, database, user uploaded content should be stored on the host system using docker volumes

Docker containers do not have a init.d deamon.

There is something called docker vortex or wormhole that helps managing connections between docker containers.

Docker does not really make sense if you deploy one app onto one host.

