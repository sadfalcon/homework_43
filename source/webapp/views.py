from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseNotAllowed, Http404
from webapp.forms import ArticleForm
from webapp.models import Article


def index_view(request):
    data = Article.objects.all()

    return render(request, 'index.html', context={
        'articles': data
    })
# Create your views here.

def article_create_view(request):
    if request.method == 'GET':

        return render(request, 'article_create.html', context={'form': ArticleForm})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            # article = Article.objects.create(**form.cleaned_data)
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                author=form.cleaned_data['author'],
                status=form.cleaned_data['status']
            )
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


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
        errors = {}
        article.title = request.POST.get('title')
        if not article.title:
            errors['title'] = 'This field is required'
        article.text = request.POST.get('text')
        if not article.text:
            errors['text'] = 'This field is required'
        article.author = request.POST.get('author')
        if not article.author:
            errors['author'] = 'This field is required'

        if errors:
            return render(request, 'article_update.html', context={
                'article': article,
                'errors': errors
            })
        article.save()
        return redirect('article_view', pk=article.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])