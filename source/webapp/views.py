from django.shortcuts import render, redirect
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
        return redirect(f'/article/?pk={article.pk}')
    else:
        HttpResponseNotAllowed(permitted_methods=['GET','POST'])




def article_view(request):
    article_id = request.GET.get('pk')
    article = Article.objects.get(pk=article_id)
    context = {'article': article}
    return render(request, 'article_view.html', context)