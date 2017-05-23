from django import forms


class ProfilForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    old_password = forms.CharField(max_length=100,
                                   widget=forms.PasswordInput, required=False)
    new_password = forms.CharField(max_length=100,
                                   widget=forms.PasswordInput, required=False)


class AddJob(forms.Form):
    image_path = forms.ImageField(required=False)


class ChangeStatus(forms.Form):
    status = forms.IntegerField(widget=forms.HiddenInput)
