from django.conf.urls import include, url
from rest_framework import routers

from news_scrappy import views
from news_scrappy.api import api_views

urlpatterns = [
    # Main page
    url(r'^$', views.main_page),

    # API URL
    url(r'^api/query/$', api_views.NewsQuery.as_view(), name='news_query'),
]
