# by Patrick Kranzlmüller

* Releasing their inhouse CMS. Named after [Luis Vola][1]
* Giving a quick overview of the functionality of Django-Vola.
    * Small project: just ~1.000 lines of code.
* see [his repository][2]
* Basic Feature Set:
    * Most work was customizing the admin: Allowing the user to add multiple
      Plugins to a Container.
    * A Container is available by having an url.
    * Plugins are simple Python-Classes (including `render()` and `data()`
      methods) and must be implemented by the project's developer.
    * CMS also includes `Preview` and `Publish` functionality out-of-the-box.


[1]: http://en.wikipedia.org/wiki/Louis_Vola
[2]: https://github.com/sehmaschine/django-vola
