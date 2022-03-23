from django.urls import include, path

from . import views

urlpatterns = [
    path('clients/create', views.person_add),
    path('list', views.person_list)
]