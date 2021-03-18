from users.models import User
from rest_framework import viewsets
from rest_framework import permissions
from serializers.serializers import (
    UserSerializer,
    DoctorSerializer,
    TeiderSerializer,
    AppointmentSerializer,
    QuerySerializer,
    WalletFundingSerializer,
    WalletWithdrawalSerializer,
)

from doctors.models import Doctor2
from teiders.models import Teider2
from appointments.models import Appointment
from queries.models import Query
from transactions.models import WalletFunding, WalletWithdrawal

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Doctor2.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

class AppointmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class QueryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    permission_classes = [permissions.IsAuthenticated]

class WFViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = WalletFunding.objects.all()
    serializer_class = WalletFundingSerializer
    permission_classes = [permissions.IsAuthenticated]

class WWViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = WalletWithdrawal.objects.all()
    serializer_class = WalletWithdrawalSerializer
    permission_classes = [permissions.IsAuthenticated]