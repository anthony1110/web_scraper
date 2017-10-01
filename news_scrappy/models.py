# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import Document, StringField


class NewsContent(Document):
    # visible field
    article_text = StringField()
    article_headline = StringField()
    article_url = StringField()
    article_tag = StringField()
