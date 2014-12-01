from django.conf import settings

SETTINGS_USER = getattr(settings, 'MARKDOWN_CONFIG', {})
SETTINGS_DEFAULT = {
    'width': "100%",
    'height': 300,
    'locale': None,
    'boostrap_cdn': True
}

markdown_config = SETTINGS_DEFAULT.copy()
markdown_config.update(SETTINGS_USER)
