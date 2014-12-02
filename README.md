Django Bootstrap Markdown
=========================

Django Bootstrap Markdown is a simple plugin that allows you to integrate the simple yet powerful [bootstrap-markdown](http://toopay.github.io/bootstrap-markdown/) into your django forms.

Installation
------------

You can install it by using ```pip```:
```
pip install django-bootstrap-markdown-editor
```

Then adding it in your ```INSTALLED_APPS``` inside your ```settings.py``` file:

```python
INSTALLED_APPS = (
    ...
    'bootstrap_markdown',
)
```

And then do a ```./manage.py syncdb```.

Integration
-----------

The integration is quite simple, like in the example below:

```python
from django import forms
from bootstrap_markdown.widgets import MarkdownEditor

class TestForm(forms.Form):

    title = forms.CharField()
    content = forms.CharField(widget=MarkdownEditor(
        attrs={'id': 'content'}))
```

You only need to import the widget and then, in the desired field, add the class with its options. More integration will be coming soon.

Settings
--------

You can also add standard settings to all the editors.

```python
MARKDOWN_CONFIG = {
    'width': "100%",
    'height': 300,
    'locale': None,
    'boostrap_cdn': True
}
```

| Name | Description          |
| ------------- | ----------- |
| width      | **(int/string)** Set the container's width by pixels (300) or percentage (100%). _(default: "100%")_ |
| height     | **(int/string)** Set the container's height by pixels (300) or percentage (100%). _(default: 300)_ |
| locale     | **(string)** Set the editor's language. Languages available: spanish (es), arabic (ar), german (de), french (fr), japanese (ja), korean (kr), norwegian (nb), dutch (nl), russian (ru), swedish (sv), turkish (tr), ukranian (ua), chinese (zh). _(default: none)_ |
| bootstrap_cdn | **(bool)** Use [bootstrapcdn](http://bootstrapcdn.com) to bring the stylesheet, jQuery and javascripts of the plugin. Else you can load them on your own. _(default: True)_ |


Or you can customize each widget:

```python
content = forms.CharField(widget=MarkdownEditor(
        attrs={
            'id': 'content',
            'width': 500,
            'height': 150,
            'autofocus': False,
            'resize': 'both',
            'icon': 'fa',
            'footer': 'Made with love <3',
            'fullscreen': True
        }))
```

| Name | Description          |
| ------------- | ----------- |
| autofocus | Indicates that editor will focused after instantiated. (default: False) |
| resize | Option to disable or change the resize property, possible values **none**, **both**, **horizontal**, **vertical**. **This is currently only supported on limited browsers.** _(default: none)_ |
| icon | The icon library to use. Glyphicons (glyph) and Font Awesome (fa) are supported. In order to use Font Awesome properly, you'll need to [include Font Awesome stylesheet](http://fontawesome.io/get-started/) yourself. _(default: glyph)_ |
| footer | **(string)** Footer dom. Can be string or callback. _(default: None)_ |
| fullscreen | **(bool)** Enable the fullscreen mode. _(default: False)_ |

Disclaimer
----------

This plugin does not handle the markdown rendering outside the widget itself. There are several libraries that can be used to achieve this:

 - [Misaka](https://github.com/FSX/misaka)
 - [Hoep (Based on Hoedown)](https://github.com/Anomareh/Hoep)
 - [Markdown](https://github.com/waylan/Python-Markdown)
 - [Markdown2](https://github.com/trentm/python-markdown2)
 - [Mitsune](https://github.com/lepture/mistune)

Contribute
----------

Feel free to add issues and make pull requests. But **do not add changes to the bootstrap-markdown plugin**. I'll always use the main repo as the source of any update.

License
-------

```
Copyright (c) 2014, Leandro Poblet
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

 - Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

 - Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

 - Neither the name of the copyright holder nor the names of its contributors
   may be used to endorse or promote products derived from this software without
   specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```