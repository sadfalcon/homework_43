from django.shortcuts import render, redirect
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
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context)