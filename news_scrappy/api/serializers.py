from rest_framework_mongoengine.serializers import DocumentSerializer

from news_scrappy.models import NewsContent


class NewsContentSerializer(DocumentSerializer):

    class Meta:
        model = NewsContent
        fields = ('id', 'article_text', 'article_headline', 'article_url', 'article_tag')
