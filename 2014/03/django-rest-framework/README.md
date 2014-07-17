# Django Rest-Framework

* *speaker* Christian Kohout
* Django-Freelancer
* http://www.getaweb.at/
* Github: https://github.com/kohout
* *slides*: http://prezi.com/ohwwohhdbbqg/first-steps-in/
* *transcript*: [./notes/transcript.txt]
* *code*: [./code]

http://www.django-rest-framework.org/

## Notes

* helps creating RESTful APIs (GET, PUT, PATCH, DELETE Requests).
* Content-Type specific responses (json vs. xml vs. custom html).
* Many out-of-the box features (request throttling, authentication, permission-management).
* "Automatically" creates interactive API documentation.

## Questions & Answers
* How to deal with multiple versions?
    * Create seperate django-apps for new major version.
    * Introduce version prefixes (/api/v1/...).
    * Deprecate older API versions (e.g. only supporting one legacy api version and
      the currently active one)


