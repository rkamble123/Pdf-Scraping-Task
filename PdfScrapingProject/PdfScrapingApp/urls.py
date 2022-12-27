from django.urls import path
from . import views

urlpatterns = [
    path('',views.insert_data.as_view(),name = 'insert_data')
]