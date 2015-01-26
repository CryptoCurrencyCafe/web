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

MENUITEMS = (
#             ('Syllabus', 'http://rust-class.org/pages/syllabus.html'),
             ('<b>Forum</b>', '/pages/forum.html'),
             ('&middot', '/'),
             ('PS0', '/pages/ps0.html'),
             ('<b>Project 1</b>', '/pages/project1.html'),
             ('&middot', 'http://rust-class.org/'),
             ('<b>Calendar</b>', 'https://www.google.com/calendar/embed?src=rmjagdrnmu3a9h2q5199lg4t28%40group.calendar.google.com&ctz=America/New_York"'),
             ('<b>Resources</b>', '/pages/resources.html'))
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
