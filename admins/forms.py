from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import  Profile
from users.models import User

from cloudinary.forms import CloudinaryFileField

# class AdminsForm(UserCreationForm):
#     email = forms.EmailField()
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
    

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']

# class ProfileUpdateForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = ['image']




class AdminSignUpForm(UserCreationForm):
    image = CloudinaryFileField(
        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'admin_pics'
       }
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['fullname', 'email', 'phone_no', 'image', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user


class AdminUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['fullname', 'email', 'phone_no', 'image']