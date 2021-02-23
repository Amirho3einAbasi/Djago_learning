from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
import django.http
from .forms import form_login, form_register

user = get_user_model()


def home_page(request):
    context = {
        'name': 'amir abasi',
        'title': 'صفحه ی اصلی سایت'
    }
    return render(request, 'html_django.html', context)


def next_page(request):
    return django.http.HttpResponse('hi my people im amir abasi and im a boss of the world in the future')


def login_paige(request):
    form2 = form_login(request.POST)
    context = {
        'form': form2,
        'title': 'صفحه ورود به سایت', 'header': 'login in to the site'
    }
    if form2.is_valid():
        print(form2.cleaned_data)
        user_login = authenticate(request, username=form2.cleaned_data.get('name'),password=form2.cleaned_data.get('password'))
        if user_login is not None:
            login(request, user_login)
            return redirect('nextPage/')

        else:
            print('error')
    return render(request, 'login_form_2.html', context)


def register_paige(request):
    form = form_register(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        user.objects.create_user(username=form.cleaned_data.get('name'), email=form.cleaned_data.get('email'),
                                 password=form.cleaned_data.get('password'))
    context = {
        'form': form,
        'title': 'Register paige'
    }

    return render(request, 'register_form.html', context)


