import requests
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Scrapy API in command.'

    def add_arguments(self, parser):
        parser.add_argument('--host', type=str, help="URL that need to be query.")
        parser.add_argument('--query_any', type=str, help="keyword to query any word in for crawling info.")
        parser.add_argument('--query_article_text', type=str, help="keyword to query article text")
        parser.add_argument('--query_article_headline', type=str, help="keyword to query article headline")
        parser.add_argument('--query_article_tag', type=str, help="keyword to query article tag.")

    def handle(self, *args, **options):
        default_url = options['host'] + "/news_scrappy/api/query/"

        if 'query_any' in options and options['query_any']:
            url = default_url + "?query_any=" + options['query_any']
        elif 'query_article_text' in options and options['query_article_text']:
            url = default_url + "?query_article_text=" + options['query_article_text']
        elif 'query_article_headline' in options and options['query_article_headline']:
            url = default_url + "?query_article_headline=" + options['query_article_headline']
        elif 'query_article_tag' in options and options['query_article_tag']:
            url = default_url + "?query_article_tag=" + options['query_article_tag']

        response = requests.get(url)
        self.stdout.write(self.style.SUCCESS('Query result = "%s"' % response.text))
        self.stdout.write(self.style.SUCCESS('Query status code = "%s"' % response.status_code))
        self.stdout.write(self.style.SUCCESS('Query number of results"%s"' % len(response.json())))
