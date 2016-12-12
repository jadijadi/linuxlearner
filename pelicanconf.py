#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'jadi'
SITENAME = u'Linux Learner'
SITESUBTITLE = u'Free LPIC 1 book, lessons and videos'
SITEURL = u'http://linuxlearner.net'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

THEME = "themes/twitchy"
#DISQUS_SITENAME = 'LinuxLearner'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
DISPLAY_TAGS_INLINE = True
#FEED_ALL_RSS = True
#FEED_ALL_ATOM = True

FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]

DISPLAY_RECENT_POSTS_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
