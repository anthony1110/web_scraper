# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def beautify_text(text):
    text = str(text).replace("\n", " ").strip()
    return text


def correct_bbc_article_link_to_full_path(url):

    url = str(url).strip()
    if not url.startswith('http'):
        url = 'http://www.bbc.com' + url
    return url
