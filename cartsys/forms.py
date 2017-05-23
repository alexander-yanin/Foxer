from django import forms


class AddToCart(forms.Form):
    pict = forms.IntegerField(widget=forms.HiddenInput)


class RemoveFromCart(forms.Form):
    pict = forms.IntegerField(widget=forms.HiddenInput)
