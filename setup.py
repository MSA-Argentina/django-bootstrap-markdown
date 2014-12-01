from setuptools import setup, find_packages

MODULE_NAME = "django-bootstrap-markdown"

setup(
    name = MODULE_NAME,
    packages = find_packages(),
    include_package_data=True,
    version = "1.0",
    description = "An useful editor wrapped up in bootstrap for your forms",
    author = "Leandro Poblet",
    author_email = "leandrodrhouse@gmail.com",
    url = "http://leandropoblet.com/",
    keywords = ["django", "markdown", "editor"],
    install_requires = ['django',],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
