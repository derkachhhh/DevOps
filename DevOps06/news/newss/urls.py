from django.urls import path
from . import views
from .views import authors_list, all_news

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', all_news, name='news_list'),
    path('news/<int:new_id>/', views.news_detail, name='news_detail'),
    path('authors/', authors_list, name='authors'),
    path('authors/<int:author_id>/news/', views.author_news, name='author_articles'),
]