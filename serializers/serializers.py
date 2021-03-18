from django.contrib.auth.models import User, Group
from rest_framework import serializers

from users.models import User
from doctors.models import Doctor2
from teiders.models import Teider2
from appointments.models import Appointment
from queries.models import Query
from transactions.models import WalletFunding, WalletWithdrawal


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('fullname', 'email', 'phone_no', 'image', 'is_admin', 'is_doctor', 'is_teider')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor2
        fields = '__all__'

class TeiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teider2
        fields = '__all__'

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class WalletWithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletWithdrawal
        fields = '__all__'

class WalletFundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletFunding
        fields = '__all__'