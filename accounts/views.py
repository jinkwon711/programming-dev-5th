from django.shortcuts import render
from django.conf import settings
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.shortcuts import redirect, render
import random
from django.contrib import messages




def register(request):
    ran_number=int(random.random()*5)
    print(ran_number)
    pic_dir = "/static/img/{}.jpg".format(ran_number)
    answerdict = { 1:"4073", 2:"4030", 3 :"1232", 4:"1284" , 0:"9725"}
    answer =answerdict.get(ran_number)
    print(answer)

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            quiz_answer = form.cleaned_data.get("quiz_answer")
            if quiz_answer == answer:
                form.save()
            else:
                messages.warning(request,"확인문자를 잘못입력하셨습니다")
                return redirect(".")
        return redirect('/')

    else:
        form = RegistrationForm()
    context = {
        "form":form,
        "pic_dir": pic_dir,
    }

    return render(request, 'accounts/register.html', context)



