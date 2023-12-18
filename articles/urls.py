from django.conf.urls import url
from django.urls import re_path
from django.views.generic import ListView, DetailView
from articles.models import Articles

urlpatterns = [
    re_path(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:30], template_name="articles/articles.html")),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model = Articles, template_name = "articles/article.html"))
]