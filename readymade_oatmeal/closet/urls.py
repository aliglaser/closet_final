from django.contrib import admin
from django.urls import path

from . import views


app_name = "closet"

urlpatterns = [
	path('', views.closet, name="closet"),
	path('closet2/', views.closet2, name="closet2"),
	path('ootd/', views.ootdview, name="ootd"),
	path('clear/', views.clear_database, name='clear_database'),
	path('basic-upload/', views.BasicUploadView.as_view(), name='basic_upload'),
	path('<int:pk>/', views.DetailView.as_view(), name="detail"),
	path('new/', views.clothes_reg, name='new'),
]


