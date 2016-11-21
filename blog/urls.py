from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^admin_test$', views.m_admin_test),
]