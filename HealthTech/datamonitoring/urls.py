# urls.py
from django.urls import path
from . import views
from .views import VitalSignsList, VitalSignsDetail, VitalSignsDelete, VitalSignsUpload

urlpatterns = [
    path('upload-data/', views.upload_data, name='upload_data'),
    path('vitalsigns/', VitalSignsList.as_view()),
    path('vitalsigns/<int:pk>/', VitalSignsDetail.as_view(), name='vitalsigns-detail'),
    path('<int:pk>/delete/', VitalSignsDelete.as_view(), name='vitalsigns_delete'),
    path('upload/', VitalSignsUpload.as_view(), name='vitalsigns_upload'),
]   

