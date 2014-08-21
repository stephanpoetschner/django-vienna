# X-Sendfile – File-Downloads, Custom Permissions, ...

* *speaker:* Clemens Pleban
* Senior Developer at [BDF-net](www.bdf-net.com) and Django-Freelancer
* *slides*: ?

## Notes

### Nginx

Add to your `nginx.conf`

    location /projectfiles/ {
        internal;
        root /var/projectfiles/;
    }
    
    
In your Django-App:
Additional Header `X-Accel-Redirect`. (Apache needs `X-Sendfile` header.)

Optional:
Use `Content-Disposition`-Header to force direct download or opening PDF's inside the browser (Chrome).

See Django-App for reference implementation: https://github.com/johnsensible/django-sendfile