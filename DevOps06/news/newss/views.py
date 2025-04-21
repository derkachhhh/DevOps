from django.shortcuts import render, get_object_or_404
from .models import News, Author


# views.py
def home(request):
    latest_news = News.objects.all().order_by('-pub_date')[:6]
    return render(request, 'news/home.html', {'latest_news': latest_news})


def all_news(request):
    news_list = News.objects.all().order_by('-pub_date')
    return render(request, 'news/all_news.html', {'news_list': news_list})


def news_detail(request, new_id):
    news_item = get_object_or_404(News, id=new_id)
    return render(request, 'news/news_details.html', {'news': news_item})


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'news/authors.html', {'authors': authors})


def author_news(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    author_news = News.objects.filter(author=author).order_by('-pub_date')
    return render(request, 'news/author_news.html', {'author': author, 'author_news': author_news})