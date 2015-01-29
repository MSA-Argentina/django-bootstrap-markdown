from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from .settings import markdown_config

__all__ = ['MarkdownEditor']

class MarkdownEditor(forms.Textarea):

    def render(self, name, value, attrs=None):

        opts = {
            'autofocus': "true" if 'autofocus' in self.attrs else "false",
            'width': self.attrs['width'] if 'width' in self.attrs\
                                        else markdown_config['width'],
            'height': self.attrs['height'] if 'height' in self.attrs\
                                        else markdown_config['height'],
            'resize': self.attrs['resize'] if 'resize' in self.attrs else "none",
            'icon': self.attrs['icon'] if 'icon' in self.attrs else "glyph",
            'footer': self.attrs['footer'] if 'footer' in self.attrs else "",
            'fullscreen': "true" if 'fullscreen' in self.attrs else "false",
            'locale': '',
        }
        boostrap_cdn = False
        if markdown_config['boostrap_cdn']:
            boostrap_cdn = True

        if markdown_config['locale'] is not None:
            locale = 'bootstrap_markdown/locale/bootstrap-markdown.{}.js'\
                .format(markdown_config['locale'])
            opts['locale'] = markdown_config['locale']
        else:
            locale = None

        return mark_safe(render_to_string('bootstrap_markdown/base_widget.html',
            {'boostrap_cdn': boostrap_cdn, 'locale': locale,
            'id': self.attrs['id'], 'opts': opts,
            'element': super(MarkdownEditor, self).render(name, value, attrs)}))
