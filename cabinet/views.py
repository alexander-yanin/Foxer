from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from Foxer.utils import base_args_cabinet, get_user
from authsys.models import User
from picture.models import Picture
# from .models import Sale
from .forms import ProfilForm, AddJob, ChangeStatus

import os


# Create your views here.
def home_cabinet(request):
    args = base_args_cabinet(request)
    if args['login']:
        form = ChangeStatus(request.POST or None)
        if form.is_valid():
            user = User.objects.get(login=args['login'])
            user.status = form.cleaned_data['status']
            user.save()
            return HttpResponseRedirect(reverse('cabinet:home_cabinet',
                                                args=()))
        args['form'] = ChangeStatus({'status': 0 if args['status'] else 1})
        return render(request, 'cabinet/base_cabinet.html', args)
    return HttpResponseRedirect(reverse('authsys:home_auth', args=()))


def profil(request):
    args = base_args_cabinet(request)
    if args['login']:
        user = get_user(request)
        form = ProfilForm(request.POST or None)
        if form.is_valid():
            user.name = form.cleaned_data['first_name']
            user.surname = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            if user.password == form.cleaned_data['old_password']:
                if form.cleaned_data['new_password'] != '':
                    new_password = form.cleaned_data['new_password']
                    user.password = new_password
                    request.session['password'] = new_password
                else:
                    args['password_error'] = 'пароль не может быть пустым'
            elif form.cleaned_data['old_password'] == '':
                pass
            else:
                args['password_error'] = 'неверный пароль'
            user.save()
            data_user = {'first_name': form.cleaned_data['first_name'],
                         'last_name': form.cleaned_data['last_name'],
                         'email': form.cleaned_data['email']}
            args['form'] = ProfilForm(data_user)
            args['result_message'] = 'данные успешно изменены'
            return render(request, 'cabinet/profil.html', args)
        else:
            data_user = {'first_name': user.name,
                         'last_name': user.surname,
                         'email': user.email}
            args['form'] = ProfilForm(data_user)
            return render(request, 'cabinet/profil.html', args)
    return HttpResponseRedirect(reverse('authsys:home_auth', args=()))


def upload(request):
    args = base_args_cabinet(request)
    form = AddJob(request.POST and request.FILES or None)
    if args['login']:
        user = get_user(request)
        if form.is_valid():
            img = request.FILES['image_path']
            p = Picture(user=user, name=img.name, path=img)
            p.save()
            return HttpResponseRedirect(reverse('cabinet:upload', args=()))
        args['form'] = AddJob({'author': user.pk})
        return render(request, 'cabinet/upload.html', args)
    return HttpResponseRedirect(reverse('authsys:home_auth', args=()))


def publication(request):
    args = base_args_cabinet(request)
    if args['login']:
        args['publication'] = Picture.objects.filter(~Q(published_date=None),
                                                     user__login=args['login'])
        return render(request, 'cabinet/publication.html', args)
    return HttpResponseRedirect(reverse('authsys:home_auth', args=()))


def delete_publication(request, pk):
    args = base_args_cabinet(request)
    if args['login']:
        p = Picture.objects.get(user__login=args['login'], pk=pk)
        os.remove('media/%s' % p.path)
        p.delete()
        return HttpResponseRedirect(reverse('cabinet:publication', args=()))
    return HttpResponseRedirect(reverse('authsys:home_auth', args=()))


def sale(request):
    args = base_args_cabinet(request)
    if args['login']:
        args['sales'] = Picture.objects.filter(~Q(sale_count=0),
                                               user__login=args['login'])
        return render(request, 'cabinet/sale.html', args)
    return HttpResponseRedirect(reverse('authsys:home_auth', args=()))


def purchase(request):
    args = base_args_cabinet(request)
    if args['login']:
        args['purchases'] = Picture.objects.filter(
            sale__user__login=args['login'])
        print(args['purchases'])
        return render(request, 'cabinet/purchase.html', args)
    return HttpResponseRedirect(reverse('authsys:home_auth', args=()))
