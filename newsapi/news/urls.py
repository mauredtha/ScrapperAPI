from django.urls import path
from django.conf.urls import handler404
from rest_framework.schemas import get_schema_view
from news.views import scrape, CreateView, ListHeadlineView, HeadlineDetail, custom404

handler404 = custom404

urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('news/', ListHeadlineView.as_view(), name="list"),
  path('news/add', CreateView.as_view(), name="create"),
  path('news/<int:pk>', HeadlineDetail.as_view(), name="detail"),
  path('', get_schema_view(
        title="News Scraper API",
        description="API for scraping news headlines, to show all list headlines, edit the details headline and delete the headlines",
        version="1.0.0"
    ), name='openapi-schema'),
]