# Practical SSL for web devs

Disclaimer: I am no security expert – just my personal experience with ssl.

## Why?

* Hide your user's traffic
    * Might be on Wireless LAN.
    * Might be at work and look at new job offers.
    * Traffic might be logged by third party (by the employer, by the provider,
      by the NSA, ...)

* Hide your login credentials! [2nd most common attack vector][1]
    * Django-Admin interface
    * Your login-page
    * Your mobile Application

* Making Man-In-the-Middle Attacks much harder.

* It's a sane default.
    * [EFF recommends it.][2]
    * [Google Search sets SSL for logged-in users as default.][3]
    * [Facebook is doing it too][4]

[1]: https://www.owasp.org/index.php/Top_10_2013-A2-Broken_Authentication_and_Session_Management
[2]: https://www.eff.org/https-everywhere/deploying-https
[3]: http://googleblog.blogspot.co.at/2011/10/making-search-more-secure.html
[4]: https://www.facebook.com/notes/facebook/a-continued-commitment-to-security/486790652130

## Simplified Steps

* Generate your key/certificate signing request.
* Pay official authority for validating your identity and for signing your certificate.
    * Certificates for free at [StartSSL][5], but horrible interface :)
* Chain your certificate with intermediate certificates from authorities.
* Deploy chained certificates and your private key
  at your front-end webserver (nginx, apache).
* Run [Qualsys SSL lab test][6].
* Customize [Django-Settings][7].
    * `SECURE_PROXY_SSL_HEADER`: making request.is_secure() work.
    * Set `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` to `True`.
      Basically disabling Cookies for HTTP. Otherwise could be leaked.
* Customize [frontend-server][8]
    * Add `X_FORWARDED_PROTO` header.
    * Redirect HTTP traffic to HTTPS.
    * Setup HTTP Strict Transport Security (HSTS).
      Simply adding a HTTP-header field, informing the browser that this domain
      must only be accessed with ssl.
      (`Strict-Transport-Security: max-age=31536000; includeSubDomains`)
    * You could even contact browser vendors and add your HSTS policy to
      their [predefined list][9]

[5]: https://startssl.com
[6]: https://www.ssllabs.com/ssltest/analyze.html
[7]: https://docs.djangoproject.com/en/1.6/topics/security/#ssl-https
[8]: https://github.com/h5bp/server-configs-nginx
[9]: https://sites.google.com/a/chromium.org/dev/sts


## Pitfalls

(most of them personally tested, while working on an API for mobile clients)

* Not including complete certificate chain.
    * Your desktop browser might download missing intermediate certificates.
    * Intermediate certificates might already be cached from other sites.
* If you are providing an API, your mobile applications might not automatically
  follow your graceful redirects.
* HTTP compression might be disabled due to BREACH attack.
* Using Server Name Indication (SNI – SSL without dedicated IP address)
  will work for Android 2.3+
  (except when mobile developers use Apache HTTP Client library).
* Enforcing certificate validation.
  Your server-to-server calls might not validate SSL certificates:
    * Python 2.x: `urllib.urlopen`
      When opening HTTPS URLs, it does not attempt to validate the server certificate. Use at your own risk!
    * Use [`requests`-library][10]!
* SSL compression should be disabled: [CRIME attack][11]. Protecting your session cookie.
    * nginx disables [SSL compression by default][12]
* HTTP compression should be disabled. [Protecting CSRF tokens][13].

[10]: http://www.python-requests.org/en/latest/
[11]: http://security.stackexchange.com/questions/19911/crime-how-to-beat-the-beast-successor
[12]: https://www.djangoproject.com/weblog/2013/aug/06/breach-and-django/
[13]: http://nginx.org/en/CHANGES


## More details

* Basic: [Nginx/StartSSL specific guide][14]
* Advanced: [Mozilla Security/Server Side TLS Guidelines][15]
* Advanced: [Hardening your SSL ciphers][16]
* Advanced: [Overview – RSA and Elliptic Curve Cryptography][17]
* Advanced: [Forward Key Secrecy][18]: Needs DHE or ECDHE algorithms
* Expert: [Improving SSL performance][19]

[14]: http://www.westphahl.net/blog/2012/01/03/setting-up-https-with-nginx-and-startssl/
[15]: https://wiki.mozilla.org/Security/Server_Side_TLS
[16]: https://hynek.me/articles/hardening-your-web-servers-ssl-ciphers/
[17]: http://arstechnica.com/security/2013/10/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/
[18]: https://www.imperialviolet.org/2013/06/27/botchingpfs.html
[19]: https://www.imperialviolet.org/2010/06/25/overclocking-ssl.html
