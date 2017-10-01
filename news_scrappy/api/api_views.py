import datetime
import pprint

import pymongo
from django.contrib.auth.models import User
from django.utils import log
from mongoengine import Q
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from news_scrappy.api.serializers import NewsContentSerializer
from news_scrappy.models import NewsContent


class NewsQuery(APIView):
    queryset = NewsContent.objects.all()
    serializer_class = NewsContentSerializer

    def get(self, request, format=None):
        get_dict = request.GET.copy()
        query_any_value = get_dict.get('query_any')
        query_article_text_value = get_dict.get('query_article_text')
        query_article_headline_value = get_dict.get('query_article_headline')
        query_article_tag_value = get_dict.get('query_article_tag')

        query = Q()
        if query_any_value:
            query = Q(article_text__icontains=query_any_value) | Q(article_headline__icontains=query_any_value) | Q(article_tag__icontains=query_any_value)
        elif query_article_text_value:
            query = Q(article_text__icontains=query_article_text_value)
        elif query_article_headline_value:
            query = Q(article_headline__icontains=query_article_headline_value)
        elif query_article_tag_value:
            query = Q(article_tag__icontains=query_article_tag_value)

        print query
        news_obj = NewsContent.objects.filter(query)
        serializer = NewsContentSerializer(news_obj, many=True)

        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
