# -*- coding: utf-8 -*-
from rest_framework import renderers
from wkhtmltopdf.utils import wkhtmltopdf, make_absolute_paths
from tempfile import NamedTemporaryFile


class TemplateHTMLRenderer(renderers.TemplateHTMLRenderer):

    def get_template_names(self, response, view):
        """
        generic template name builder
        """
        _namespace = view.queryset.model.__module__
        _namespace = _namespace.replace('.models', '').replace('.', '/')
        _model = view.queryset.model.__name__.lower()
        _action = view.action

        return ['%(namespace)s/%(model)s/%(action)s.html' % {
            'namespace': _namespace,
            'model': _model,
            'action': _action,
        }]


class TemplatePDFRenderer(TemplateHTMLRenderer):
    """
    renders serialized data as PDF document
    """
    media_type = 'application/pdf'
    format = 'pdf'

    def get_template_names(self, response, view):
        """
        generic template name builder
        """
        _namespace = view.queryset.model.__module__
        _namespace = _namespace.replace('.models', '').replace('.', '/')
        _model = view.queryset.model.__name__.lower()
        _action = view.action

        return ['%(namespace)s/%(model)s/pdf/%(action)s.html' % {
            'namespace': _namespace,
            'model': _model,
            'action': _action,
        }]


    def _html_to_pdf(self, content):
        content = make_absolute_paths(content)
        tempfile = NamedTemporaryFile(mode='w+b', bufsize=-1, suffix='.html',
            prefix='tmp', dir=None, delete=True)

        tempfile.write(content.encode('utf-8'))
        tempfile.flush()
        options = {}
        """
        example usage of wkhtmltopdf method:

            wkhtmltopdf(pages=['/tmp/example.html'],
                        dpi=300,
                        rotation='Landscape',
                        disable_javascript=True)
        """
        return wkhtmltopdf(pages=[tempfile.name], **options)


    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        returns the default html output as pdf
        """
        content = super(TemplatePDFRenderer, self).render(
            data, accepted_media_type, renderer_context)

        return self._html_to_pdf(content)
