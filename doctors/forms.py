from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor2
from users.models import User

from django.db import transaction

from cloudinary.forms import CloudinaryFileField

class DoctorSignUpForm(UserCreationForm):
    image = CloudinaryFileField(
        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'doctor_pics'
       }
    )
    discipline = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['fullname', 'email', 'phone_no', 'discipline', 'image', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor2.objects.create(user=user, discipline=self.cleaned_data.get('discipline'), wallet_balance=0.00)
        print(self.cleaned_data.get('discipline'))
        # doctor.wallet_balance = 0.00
        # doctor.discipline = self.cleaned_data.get('discipline')

        return user


class DoctorUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['fullname', 'email', 'phone_no', 'image']

class DoctorProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Doctor2
        fields = ['discipline']