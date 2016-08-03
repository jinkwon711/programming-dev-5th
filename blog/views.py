from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect , redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .models import ZipCode, Post, Comment, Tag
from .forms import *

def post_list(request):
    qs = Post.objects.all()
    context = {
        'post_list': qs,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    qs = Post.objects.get(pk=pk)
    qs_comment = Comment.objects.filter(post_id=pk)
    qs_tags = Tag.objects.filter(post__pk = pk)
    context = {
        'post': qs,
        'comment_list': qs_comment,
        'tags': qs_tags,

    }
    return render(request, 'blog/post_detail.html', context)

def post_new(request):

    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid :
            form.save()
            return redirect('../')
    else:
        form = PostForm
    return render(request, 'blog/post_form.html', {'form' :form})


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid :
            form.save()
            return redirect('/')
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/post_form.html',{'form':form,} )

def comment_new(request, post_pk):
    if request.method =="POST":
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=post_pk)
            form.save()
            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentModelForm()
    return render(request, 'blog/comments_form.html', {'form' :form} )

def comment_edit(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method =="POST":
        form = CommentModelForm(request.POST, request.FILES, instance = comment )
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk = post_pk)
            form.save()
            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentModelForm(instance = comment)
    return render(request, 'blog/comments_form.html', {'form' :form} )




def about(request):
	return render(request, 'blog/about.html', {})


def gallery(request):
	return render(request, 'blog/gallery.html', {})


def mysum(request, x, y=0, z=0):
    return HttpResponse(int(x) + int(y) + int(z))


def mysum2(request, x):
    result = sum(int(i) for i in x.split("/"))
    return HttpResponse(result)

def zipcode(request):
    title = "우편번호 검색"
    form = ZipCodeForm(request.POST or None)
    context = {'form': ZipCodeForm, "title" : title}

    if form.is_valid():
        zipcode = form.cleaned_data.get("zipcode")
        if ZipCode.objects.filter(zipcode = zipcode).exists():
            return render(request, 'blog/zipcode_exist.html', {"AreaList": ZipCode.objects.filter(zipcode =zipcode),})
        else:
            return HttpResponseRedirect(".zipcode_error/")
# context = {"title":"유효한 우편번호입니다."}
    return render(request, 'blog/zipcode.html', context)





