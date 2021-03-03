from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.CreateTeider.as_view(), name='create-teiders'),
    path('listteiders/', views.ListTeider.as_view(), name='list-teiders'),
    path('teiders/<int:pk>/update/', views.TeiderUpdate.as_view(), name='teider-update'),
    # # path('teiders/<int:pk>/', views.TeiderDetail.as_view(), name='teider-detail'),
    path('teiders/<int:pk>/delete/', views.TeiderDelete.as_view(), name='teider-delete'),
    path('teiders/<str:email>/', views.teiddetail, name='teider-detail'),
    
]