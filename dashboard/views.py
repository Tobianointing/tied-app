from django.shortcuts import render, redirect
# from teiders.models import TeiderModel
# from doctors.models import DoctorModel
from transactions.models import WalletFunding, WalletWithdrawal
from queries.models import Query
from appointments.models import Appointment
from users.models import User

# Create your views here.
def dashboard(request):
    query = Query.objects.all()
    appointment = Appointment.objects.all()

    qaccepted = Query.objects.filter(status='accepted').count()
    qsettled = Query.objects.filter(status='settled').count()
    qbooked = Query.objects.filter(status='booked').count()
    qcancelled = Query.objects.filter(status='cancelled').count()

    # aaccepted = Appointment.objects.filter(status='accepted').count()
    asettled = Appointment.objects.filter(status='settled').count()
    abooked = Appointment.objects.filter(status='booked').count()
    acancelled = Appointment.objects.filter(status='cancelled').count()

    fund = WalletFunding.objects.all()
    teiders = User.objects.filter(is_teider=True)
    doctors = User.objects.filter(is_doctor=True)

    context = {
        'query': query,
        'appointment': appointment,

        'qaccepted': qaccepted,
        'qsettled': qsettled,
        'qbooked': qbooked,
        'qcancelled': qcancelled,

        # 'aaccepted': aaccepted,
        'asettled': asettled,
        'abooked': abooked,
        'acancelled': acancelled,

        'fund': fund,
        'teiders': teiders,
        'doctors': doctors,

    }

    return render(request, 'dashboard/dashboard.html', context)


def redirect_user_to_page(request):
    if request.user.is_admin:
        return redirect('dashboard')
    elif request.user.is_doctor:
        return redirect('doc-dashboard')

    return redirect('admins:login')