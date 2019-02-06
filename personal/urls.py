from django.conf.urls import url
from . import views

app_name = "main"

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout', views.logout_request, name='logout'),
    url(r'login/', views.login_request, name='login')
]
