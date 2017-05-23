from django.template import Context
from picture.models import Picture
from authsys.models import User


# base context for template
def base_args(request):
    args = {}
    try:
        args['login'] = request.session['login']
        pict = list(Picture.objects.filter(cart__user__login=args['login']))
        args['num_pic'] = len(pict)
    except KeyError:
        args['login'] = None
        args['num_pic'] = 0
    return args


def base_args_cabinet(request):
    args = base_args(request)
    try:
        user = get_user(request)
        purchase = list(Picture.objects.filter(sale__user=user))
        args['purchase_count'] = len(purchase)
        args['status'] = user.status
        args['balance'] = user.balance
    except KeyError:
        args['status'] = 0
        args['balance'] = 0
    return args


def get_user(request):
    return User.objects.get(login=request.session['login'],
                            password=request.session['password'])
