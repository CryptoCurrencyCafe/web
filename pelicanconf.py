#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David Evans'
SITENAME = 'Cryptocurrency Cafe'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "./bitcoin-theme"
DISPLAY_PAGES_ON_MENU = False
STATIC_PATHS = ['images', 'docs', 'resources', 'classes', 'pages', 'readings']

# Blogroll
LINKS = (# ('Pelican', 'http://getpelican.com/'),
         # ('Python.org', 'http://python.org/'),
         # ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),)
    )

# Social widget
SOCIAL = (# ('You can add links in your config file', '#'),
          # ('Another social link', '#'),)
    )
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "bitcoin-class"
GOOGLE_ANALYTICS = "UA-3775212-12"