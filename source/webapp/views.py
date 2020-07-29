from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Article
from django.http import HttpResponseNotAllowed


def index_view(request):
    data = Article.objects.all()

    return render(request, 'index.html', context={
        'articles': data
    })
# Create your views here.

def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('content')
        author = request.POST.get('author')
        article = Article.objects.create(title=title, text=text, author=author)

        #url = reverse('article_view', kwargs={'pk': article.pk})
        return redirect('article_view', pk=article.pk
                        )
    else:
        HttpResponseNotAllowed(permitted_methods=['GET','POST'])


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context)

def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'article_update.html', context={'article':article})
    elif request.method == 'POST':
        article.title = request.POST.get('title')
        article.text = request.POST.get('content')
        article.author = request.POST.get('author')
        article.save()

        return redirect('article_view', pk=article.pk
                        )
    else:
        HttpResponseNotAllowed(permitted_methods=['GET','POST'])