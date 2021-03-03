from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.CreateDoctor.as_view(), name='create-doctors'),
    path('listdoctors/', views.ListDoctor.as_view(), name='list-doctors'),
    path('doctors/<int:pk>/update/', views.doc_update, name='doctor-update'),
    path('doctors/<int:pk>/delete/', views.DoctorDelete.as_view(), name='doctor-delete'),
    path('doctors/<str:email>/', views.docdetail, name='doctor-detail'),
    path('doc_dashboard/', views.doc_dashboard, name='doc-dashboard'),
    path('doc_appointments/', views.doc_appointment, name='doc-appointments'),
    path('doc_queries/', views.doc_query, name='doc-queries'),
    path('accept/<str:email>/<int:id>/', views.doc_accept, name='doc-accept'),
    path('cancel_appointment/<int:id>/', views.cancel_appointment, name='appointment-cancel'),
    path('doctor/signup/', views.doctor_signup, name='doctor-signup'),
]