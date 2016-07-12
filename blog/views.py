from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
def about(request):
	return render(request, 'blog/about.html', {})
def gallery(reqeust):
	return render(reqeust, 'blog/gallery.html', {})
# Create your views here.
