from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

from article.models import Article
from django.shortcuts import render

from django import forms
from django.http import HttpResponseRedirect

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', ]

def home(request):
    s = "This is the Main Page."
    return HttpResponse(s)
def now(request):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    return HttpResponse(str(year) + "//" + str(month) + "//" + str(day))
def helloWorld(request):
    s = "Bad URL!!!"
    return HttpResponse(s)


# def detail(request, pk):
#     article = Article.objects.get(pk=int(pk))
#     s = """
#     <html>
#     <head></head>
#     <body>
#     <h1>{0}</h1>
#     {1}
#     </body>
#     </html>
#     """.format(article.title, article.content)
#     return HttpResponse(s)
def detail(request, pk):
    article = Article.objects.get(pk=int(pk))
    return render(request, "detail.html", {'article': article})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        return HttpResponseRedirect('/article/1')
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect('/article/' + str(new_article.pk))
        else:
            return HttpResponseRedirect('/article/1')
    form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})