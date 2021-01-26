from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('home', views.Home.as_view(), name='index'),
    path('import', views.Import.as_view(), name='import_data')
]
