#-*- coding:utf8-*-
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from models import Article
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
    try:
        post = Article.objects.all()
        paginator = Paginator(post,2)
        page = request.GET.get('page') or 1
        post_list = paginator.page(page)
        #print post.title
    except Article.DoesNotExist:
        raise Http404
    t = loader.get_template('index.html')
    c = Context({'post_list':post_list})
    return HttpResponse(t.render(c))


def detail(request, id):
    print '###############',id
    try:
        post = Article.objects.get(id=str(id))
        #print post.title
    except Article.DoesNotExist:
        raise Http404
    t = loader.get_template('single_article.html')
    c = Context({'post':post})
    return HttpResponse(t.render(c))

def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(catagory__iexact=tag)
    except Article.DoesNotExist:
        raise Http404

    t = loader.get_template('tag.html')
    c = Context({'post_list':post_list})
    return HttpResponse(t.render(c))


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            try:
                post = Article.objects.all()
                # print post.title
            except Article.DoesNotExist:
                raise Http404
            t = loader.get_template('index.html')
            c = Context({'post_list': post})
            return HttpResponse(t.render(c))
        else:
            try:
                post_list = Article.objects.filter(title__iexact=s)
            except Article.DoesNotExist:
                raise Http404

            t = loader.get_template('index.html')
            c = Context({'post_list': post_list})
            return HttpResponse(t.render(c))
    return redirect('/')
