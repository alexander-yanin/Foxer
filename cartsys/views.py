from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Sum
from picture.models import Picture
from authsys.models import User
from cartsys.models import Cart, Payment
from cabinet.models import Sale
from Foxer.utils import base_args, get_user


# Create your views here.
def home_cart(request):
    args = base_args(request)
    if args['login']:
        if request.method == 'POST':
            pictures = request.POST.getlist('selects')
            if pictures:
                cart_user = Cart.objects.get(user__login=args['login'])
                for picture in pictures:
                    p = Picture.objects.get(pk=picture)
                    cart_user.picture.remove(p)
            return HttpResponseRedirect(reverse('cartsys:home_cart', args=()))
        args['pictures'] = list(Picture.objects.filter(
            cart__user__login=args['login']))
        args['final_sum'] = Picture.objects.filter(
            cart__user__login=args['login']).aggregate(
                Sum('price'))['price__sum']
        return render(request, 'cartsys/home_cart.html', args)
    return HttpResponseRedirect(reverse('authsys:home_auth', args=()))


# def add_in_cart(request):
#     args = base_args(request)
#     if request.method == 'POST':
#         pict_pk = request.POST['pict']
#         picture = Picture.objects.get(pk=pict_pk)
#         cart_user = Cart.objects.get(user__login=args['login'])
#         cart_user.picture.add(picture)
#         cart_user.save()
#         return HttpResponseRedirect(reverse('picture:home_picture',
#                                             args=(pict_pk,)))
#     return render(request, 'picture/home.html', args)


# def delete_from_cart(request):
#     args = base_args(request)
#     if args['login']:
#         if request.method == 'POST':
#             pict_pk = request.POST['pict']
#             picture = Picture.objects.get(pk=pict_pk)
#             cart_user = Cart.objects.get(user__login=args['login'])
#             cart_user.picture.remove(picture)
#             return HttpResponseRedirect(reverse('picture:home_picture',
#                                                 args=(pict_pk,)))
#     return render(request, 'picture/home.html')


def payment(request):
    args = base_args(request)
    if args['login']:
        if request.method == 'POST':
            sales_sum = Picture.objects.filter(
                cart__user__login=args['login']).aggregate(
                    Sum('price'))['price__sum']
            user = get_user(request)
            if user.balance-sales_sum > 0:
                sales = Picture.objects.filter(cart__user__login=user.login)
                pay = Payment(user=user, cost=sales_sum)
                pay.save()
                cart = Cart.objects.get(user__login=user.login)
                user_sale = Sale.objects.get(user=user)
                for sale in sales:
                    author = User.objects.get(picture__pk=sale.pk)
                    author.balance += sale.price
                    user.balance -= sale.price
                    author.save()
                    user.save()
                    sale.sale_count += 1
                    sale.save()
                    user_sale.pictures.add(sale)
                    user_sale.save()
                    pay.picture.add(sale)
                    pay.save()
                    cart.picture.remove(sale)
            return HttpResponseRedirect(reverse('cabinet:home_cabinet',
                                                args=()))
