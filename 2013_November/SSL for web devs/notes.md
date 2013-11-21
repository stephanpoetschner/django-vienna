# Practical SSL for web devs

Disclaimer: I am no security expert. Any improvements/recommendations highly appreciated.

## Why?

* Protect our users!
    * Might be on insecure network (Wireless LAN).
    * Might look at sensitive data (being at work and look at new job offers).
    * Users tend to reuse their (weak) passwords over and over.
    * Traffic might be logged by third party (by the employer, by the provider,
      by the NSA, ...). As processing power increases, logged traffic might be decrypted.

* Protect yourself!
    * Hide your login credentials! [2nd most common attack vector][1]
    * Ever accessed your Django-Admin interface at a conference using the wireless network.

* It's your job! Leverage security by simply switching SSL on.
    * APIs for partners or mobile applications?
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
      their [predefined list][9].

[5]: https://startssl.com
[6]: https://www.ssllabs.com/ssltest/analyze.html
[7]: https://docs.djangoproject.com/en/1.6/topics/security/#ssl-https
[8]: https://github.com/h5bp/server-configs-nginx
[9]: https://sites.google.com/a/chromium.org/dev/sts


## Pitfalls

(most of them personally tested, while working on an API for mobile clients)

* Not enought testing! [Qualsys SSL lab test][6]
* Not including complete certificate chain.
    * Your desktop browser might download missing intermediate certificates.
    * Intermediate certificates might already be cached from other sites at your machine.
* If you are providing an API, your mobile applications might not automatically
  follow your graceful redirects from HTTP to HTTPS.
* Compression might/should be disabled due to possible information leakage.
    * SSL compression should be disabled: [CRIME attack][10]. Protecting your session cookie. 
      nginx disables [SSL compression by default][11].
    * HTTP compression should also be disabled – [following your Django advice][12]. 
      This will protect your CSRF tokens.
* Using Server Name Indication (SNI – SSL without dedicated IP address)
  will work for [Android][13] 2.3+ – except when mobile developers use Apache HTTP Client library.
* Enforcing certificate validation.
  Your server-to-server calls might not validate SSL certificates:
    * Python 2.x: `urllib.urlopen`
      When opening HTTPS URLs, it does not attempt to validate the server certificate. Use at your own risk!
    * Use [`requests`-library][14]!

[10]: http://security.stackexchange.com/questions/19911/crime-how-to-beat-the-beast-successor
[11]: https://www.djangoproject.com/weblog/2013/aug/06/breach-and-django/
[12]: http://nginx.org/en/CHANGES
[13]: http://developer.android.com/training/articles/security-ssl.html
[14]: http://www.python-requests.org/en/latest/


## More details

* Basic: [Nginx/StartSSL specific guide][14]
* Advanced: [Mozilla Security/Server Side TLS Guidelines][15].

        ssl_prefer_server_ciphers on;
        ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:
             ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:kEDH+AESGCM:
             ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:
             ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:
             ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:
             DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:
             DHE-DSS-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:
             ECDHE-RSA-RC4-SHA:ECDHE-ECDSA-RC4-SHA:RC4-SHA:HIGH:
             !aNULL:!eNULL:!EXPORT:!DES:!3DES:!MD5:!PSK;

* Advanced: [CloudFlare: Staying on top of TLS attacks][16]. Also read about "Forward Secrecy".

        ssl_prefer_server_ciphers on;
        ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-RC4-SHA:
            ECDHE-RSA-AES128-SHA:AES128-GCM-SHA256:RC4:HIGH:
            !MD5:!aNULL:!EDH:!CAMELLIA;
        
* Expert: [Overview – RSA and Elliptic Curve Cryptography][17]
    * breaking 228-bit RSA key: energy of boiling teaspoon of water.
    * breaking 228-bit ECC key: energy of boiling all water on earth.
    * short, fast and secure keys (256-bit ECC key comparable to 2.058-bit RSA key, but 20x faster).
* Expert: [Improving SSL performance][18]

[14]: http://www.westphahl.net/blog/2012/01/03/setting-up-https-with-nginx-and-startssl/
[15]: https://wiki.mozilla.org/Security/Server_Side_TLS
[16]: http://blog.cloudflare.com/staying-on-top-of-tls-attacks
[17]: http://arstechnica.com/security/2013/10/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/
[18]: https://www.imperialviolet.org/2010/06/25/overclocking-ssl.html
