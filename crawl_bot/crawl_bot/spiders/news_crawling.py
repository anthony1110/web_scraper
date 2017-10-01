from scrapy.spiders import BaseSpider

class NewsSpider(BaseSpider):
    name = "news_crawling"
    start_urls = ['http://www.bbc.com/']

    def parse(self, response):
        for brick in response.css('div.media__content'):
            TITLE_SELECTOR = 'h3 a ::text'
            SUMMARY_SELECTOR = 'p ::text'
            LINK_SELECTOR = '.media__title a ::attr(href)'
            TAG_SELECTOR = '.media__tag ::text'

            yield {
                'title': brick.css(TITLE_SELECTOR).extract(),
                'summary': brick.css(SUMMARY_SELECTOR).extract(),
                'link': brick.css(LINK_SELECTOR).extract(),
                'tag': brick.css(TAG_SELECTOR).extract(),
            }