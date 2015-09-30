from copy import deepcopy
from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from .settings import markdown_config

__all__ = ['MarkdownEditor']

class MarkdownEditor(forms.Textarea):

    def render(self, name, value, attrs=None):

        config = deepcopy(markdown_config)
        config.update(self.attrs)

        opts = {
            'autofocus': "true" if config.get('autofocus', False) else "false",
            'savable': "true" if config.get('savable', False) else "false",
            'hideable': "true" if config.get('hideable', False) else "false",
            'width': config['width'],
            'height': config['height'],
            'resize': config.get('resize', "none"),
            'icon': config.get('icon', "glyph"),
            'footer': config.get('footer', ""),
            'hiddenButtons': config.get('hiddenButtons', ""),
            'disabledButtons': config.get('disabledButtons', ""),
            'fullscreen': "true" if\
                               config.get('fullscreen', False) else "false",
            'locale': '',
        }
        boostrap_cdn = False
        if markdown_config['boostrap_cdn']:
            boostrap_cdn = True

        if config['locale'] is not None:
            locale = 'bootstrap_markdown/locale/'
            locale += 'bootstrap-markdown.{}.js'.format(config['locale'])
            opts['locale'] = config['locale']
        else:
            locale = None

        return mark_safe(render_to_string('bootstrap_markdown/base_widget.html',
            {'boostrap_cdn': boostrap_cdn, 'locale': locale,
            'id': self.attrs['id'], 'opts': opts,
            'element': super(MarkdownEditor, self).render(name, value, attrs)}))
