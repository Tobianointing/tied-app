from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from viewsets import viewsets

from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/v1/users', viewsets.UserViewSet, basename='user')
router.register('api/v1/doctors', viewsets.DoctorViewSet)
router.register('api/v1/appointments', viewsets.AppointmentViewSet)
router.register('api/v1/queries', viewsets.QueryViewSet)
router.register('api/v1/wf', viewsets.WFViewSet)
router.register('api/v1/ww', viewsets.WWViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('teiders/', include('teiders.urls')),
    path('doctors/', include('doctors.urls')),
    path('query/', include('queries.urls')),
    path('appointment/', include('appointments.urls')),
    path('transactions/', include('transactions.urls')),
    path('conversations/', include('conversations.urls')),
    path('', include('admins.urls')),
    path('', include('users.urls')),

    #drf urls
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
