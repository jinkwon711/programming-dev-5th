from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.http import HttpResponse
from .forms import ZipCodeForm
from django.core.exceptions import ValidationError
from .models import ZipCode
def post_list(request):
    return render(request, 'blog/post_list.html', {})


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
