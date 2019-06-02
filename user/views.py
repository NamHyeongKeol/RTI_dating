from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

from django.http import HttpResponse
from django.shortcuts import render, redirect


# from user.forms import UserCreationForm, LoginForm
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'mypage.html')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(0)
        if form.is_valid():
            print(1)
            new_user = User.objects.create_user(**form.cleaned_data)
            print(2)
            login(request, new_user)
            print(3)
            return redirect('index')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def changepassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.POST)

