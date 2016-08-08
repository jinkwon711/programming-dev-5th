from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import ZipCode, Post, Comment, Tag
from blog.forms import *
from programming.pil_image import thumbnail, square_image
from django.core.files import File
from django.db.models.signals import pre_save

# message 예제
# messages.add-message(request, messages.INFO, "Hello world")
# ->숏컷 쓰면, messages.info(request, "Hello world")



def post_list(request):
    qs = Post.objects.all()
    context = {
        'post_list': qs,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    # try:
    #     qs = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404
    # 위 네줄을 아래 한줄로 바꾸기
    qs = get_object_or_404(Post, pk=pk)
    qs_comment = Comment.objects.filter(post_id=pk)
    # 코멘트 불러올떄 post.comment_set.all로 불러와도된다 이게 더 편한듯?
    qs_tags = Tag.objects.filter(post__pk=pk)
    context = {
        'post': qs,
        'comment_list': qs_comment,
        'tags': qs_tags,

    }
    return render(request, 'blog/post_detail.html', context)

def post_new(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('../')
    else:
        form = PostForm
    return render(request, 'blog/post_form.html', {'form':form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES ,instance=post)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, })

def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        form = CommentModelForm(request.POST, request.FILES )
        if form.is_valid():
            comment = form.save(commit=False)
            # 바로 윗글을 디비에는 바로 저장하지 말라는것. 왜냐하면 post값을 지정을 안해줬음.
            # 그래서 아래에 지정을 해주는 것이다.
            comment.post = get_object_or_404(Post, pk=post_pk)
            form.save()
            messages.success(request,'새 댓글이 등록되었습니다.')  #-> 이거하고 html가서 템플릿태그등
            # return redirect('blog:post_detail', post_pk)
            return redirect(post)
            # 일단 겟 앱솔루트 url이 있는 확인하고 호출.
    else:
        form = CommentModelForm()
    return render(request, 'blog/comments_form.html', {'form': form, })

def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == "POST":
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





