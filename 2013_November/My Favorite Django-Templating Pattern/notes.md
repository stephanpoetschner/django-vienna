# by Anton Pirker

* See [Anton's Blog Post][1]

[1]: http://anton-pirker.at/django-override-block-that-was-in-included-in-parent-template/

----

## Discussion

* Which naming conventions/rules did you establish?
    * `/_includes/` subfolder for HTML snippets (templates that would not render
      a valid html page – including header-, body-tags,...)
    * `base.html` templates: getting extended 80% of time. Example:
        * `base.html`
        * `_includes/base_header.html`
    * General rule `templates` in project-global template folder.
      If a "stand-alone" app materializes (and I want to re-use the app in
      another project), add app-specific templates for having defaults after
      installing the app in another project.
    * Sometimes it's useful to pull some more template-inheritance logic into
      the view. Simply passing a string variable into the template, defining the
      parent template: `{% extends my_template_name %}` instead of
      `{% extends "path/to/file" %}`.

* [Django-Sekizai][2] – Quoting the doc: "A fresh look at blocks."
* [Django-classy-tags][3] – Quoting the docs: "making writing template tags in Django easier"

[2]: https://django-sekizai.readthedocs.org/en/latest/
[3]: https://django-classy-tags.readthedocs.org/en/latest/




