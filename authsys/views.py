from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import RegForm, AuthForm
from .models import User
from cabinet.models import Sale
from cartsys.models import Cart
from Foxer.utils import base_args

import os


# Create your views here.
def home_auth(request):
    args = base_args(request)
    try:
        if request.session['login']:
            return HttpResponseRedirect(reverse('picture:home', args=()))
    except KeyError:
        pass
    args['form'] = AuthForm()
    return render(request, 'authsys/auth.html', args)


def reg(request):
    args = base_args(request)
    try:
        if request.session['login']:
            return HttpResponseRedirect(reverse('picture:home', args=()))
    except KeyError:
        pass
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if not User.objects.filter(login=login).exists():
                user = User(login=login, email=email, password=password)
                user.save()
                cart = Cart(user=user)
                cart.save()
                sale = Sale(user=user)
                sale.save()
                request.session.set_expiry(60*60*24*30)
                request.session['login'] = login
                request.session['password'] = password
                os.mkdir('media/authors/%s' % login)
                os.mkdir('media/buyer/%s' % login)
                return HttpResponseRedirect(reverse('picture:home', args=()))
    else:
        args['form'] = RegForm()
    return render(request, 'authsys/reg.html', args)


def login(request):
    args = base_args(request)
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            if User.objects.filter(login=login, password=password).exists():
                request.session.set_expiry(60*60*24*30)
                request.session['login'] = login
                request.session['password'] = password
                return HttpResponseRedirect(reverse('picture:home', args=()))
    else:
        args['form'] = AuthForm()
    return render(request, 'authsys/auth.html', args)


def logout(request):
    try:
        del request.session['login']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('picture:home', args=()))
