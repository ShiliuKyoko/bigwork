from django.shortcuts import render,redirect,Http404
from Tadmin.models import Article,Comment
from Tadmin.form import CommentForm,LoginForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

def Testadmin(request):
    context = {}
    # if request.method == 'GET':
    #     form = CommentForm
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         content = form.cleaned_data['content']
    #         c = Comment(name=name,content=content)
    #         c.save()
    #         return redirect(to='index')
    if request.user.is_authenticated():
        queryset = request.GET.get('tag')
        if queryset:
            article_list = Article.objects.filter(tag=queryset)
        else:
            article_list = Article.objects.order_by('-id')

        comment_list = Comment.objects.all()
        page_robot = Paginator(article_list,3)
        page_geter = request.GET.get('page')
        try:
            article_list = page_robot.page(page_geter)
        except EmptyPage:
            article_list = page_robot.page(page_robot.num_pages)
            # raise Http404('Such a fool!')
        except PageNotAnInteger:
            article_list = page_robot.page(1)
        context['article_list'] = article_list
    else:
        return redirect(to='error_page')


    # context['comment_list'] = article_list
    # context['form'] = form

    return render(request,'index.html',context)



def detail(request,page_num,error_form=None):

    context = {}
    form = CommentForm
    # if request.method == 'GET':
    #     form = CommentForm
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         content = form.cleaned_data['content']
    #         article = Article.objects.get(id=page_num)
    #         c = Comment(name=name,content=content,belong_to=article)
    #         c.save()
    #         return redirect(to='detailaaa',page_num=page_num)

    if request.user.is_authenticated():
        article = Article.objects.get(id=page_num)
        best_commnet = Comment.objects.filter(best_commnet=True,belong_to=article)
        comment = Comment.objects.filter(best_commnet=False)
        context['Not_best'] = comment
        if best_commnet:
            context['best_commnet'] = best_commnet[0]
        context['article'] = article
        # context['form'] = form
        if error_form is not None:
            context['form'] = error_form
        else:
            context['form'] = form

    else:
        return redirect(to='error_page')
    return render(request,'detail.html',context)


def detail_commnetPOST(request,page_num):
    context = {}
    article = Article.objects.get(id=page_num)
    form = CommentForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        c = Comment(name=title,content=content,belong_to=article)
        c.save()
    else:
        return detail(request, page_num=page_num, error_form=form)

    return redirect(to='detail',page_num=page_num)

def index_login(request):
    context = {}
    if request.method == 'GET':
        form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to='index')
    context['form'] = form
    return render(request, 'register_login.html', context)

def index_register(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    context['form'] = form
    return render(request, 'register_login.html', context)

def error_page(request):
    return render(request,'error_page.html')

def test(request):
    if request.user.is_authenticated():
        return render(request,'test.html')
    else:
        return redirect(to='error_page')

def table_page(request):
    if request.user.is_authenticated():
        return render(request,'table.html')
    else:
        return redirect(to='error_page')


def aboutme(request):
    return render(request,'about.html')
