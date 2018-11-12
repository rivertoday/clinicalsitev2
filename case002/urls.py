# coding:utf-8
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'case002'
urlpatterns = [
    path('about/', views.about, name='about'),
    path('datainput/', views.datainput, name='datainput'),
    path('datamodify/<int:people_id>/', views.datamodify, name='datamodify'),
    path('datainput1/<int:people_id>/', views.datainput1, name='datainput1'),
    path('datainput2/<int:people_id>/', views.datainput2, name='datainput2'),
    path('datainput3/<int:people_id>/', views.datainput3, name='datainput3'),
    path('datainput4/<int:people_id>/', views.datainput4, name='datainput4'),
    path('datalist/', views.datalist, name='datalist'),
    path('datadetail/<int:archive_id>/', views.datadetail, name='datadetail'),
    path('dataana/', views.dataana, name='dataana'),
    path('about/', views.about, name='about'),
    path('bingo/', views.bingo, name='bingo'),
    path('permhint', views.permhint, name='permhint'),
    path('suggestinfo1', views.suggestinfo1, name='suggestinfo1'),
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)