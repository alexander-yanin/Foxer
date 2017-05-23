from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from Foxer.utils import base_args
from picture.models import Picture
from cartsys.models import Cart
from cartsys.forms import AddToCart, RemoveFromCart

import datetime
import random


# Create your views here.
def home(request):
    args = base_args(request)
    end = timezone.now()
    start = end - datetime.timedelta(days=1)
    new_pubs = list(Picture.objects.filter(published_date__range=(start, end)))
    random.shuffle(new_pubs)
    args['new_pubs'] = new_pubs[:6]
    args['lid_sales'] = list(Picture.objects.order_by('sale_count'))[:6]
    return render(request, 'picture/home.html', args)


def home_picture(request, pk):
    args = base_args(request)
    args['picture'] = Picture.objects.get(pk=pk)
    if Cart.objects.filter(user__login=args['login'],
                           picture=args['picture'].pk).exists():
        args['form'] = RemoveFromCart({'pict': args['picture'].pk})
        args['exist'] = True
    else:
        args['form'] = AddToCart({'pict': args['picture'].pk})
        args['exist'] = False
    if request.method == 'POST':
        if args['login']:
            if request.POST['operation'] == 'delete':
                pict_pk = request.POST['pict']
                picture = Picture.objects.get(pk=pict_pk)
                cart_user = Cart.objects.get(user__login=args['login'])
                cart_user.picture.remove(picture)
            elif request.POST['operation'] == 'add':
                pict_pk = request.POST['pict']
                picture = Picture.objects.get(pk=pict_pk)
                cart_user = Cart.objects.get(user__login=args['login'])
                cart_user.picture.add(picture)
                cart_user.save()
            return HttpResponseRedirect(reverse('picture:home_picture',
                                                args=(pict_pk,)))
    return render(request, 'picture/picture.html', args)
