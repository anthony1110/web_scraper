# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from news_scrappy.models import NewsContent
from news_scrappy.utils import beautify_text, correct_bbc_article_link_to_full_path


class CrawlBotPipeline(object):
    def process_item(self, item, spider):
        article_text = beautify_text(item.get('summary')[0]) if len(item.get('summary')) > 0 else ''
        article_headline = beautify_text(item.get('title')[0]) if len(item.get('title')) > 0 else ''
        article_url = correct_bbc_article_link_to_full_path(item.get('link')[0]) if len(item.get('link')) > 0 else ''
        article_tag = beautify_text(item.get('tag')[0]) if len(item.get('tag')) > 0 else ''
        news = NewsContent(article_headline=article_headline,
                           article_text=article_text,
                           article_url=article_url,
                           article_tag=article_tag)
        news.save()

        return item
