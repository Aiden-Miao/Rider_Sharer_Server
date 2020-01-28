from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'uper'
urlpatterns = [
    path('', TemplateView.as_view(template_name="uper/index.html"), name='index'),
    path('register/', TemplateView.as_view(template_name="uper/register.html"), name='register'), 
    path('register_process/', views.register_process, name='register_process'),
    path('login/', views.login, name='login'),
    path('main_page/', views.main_page, name='main_page'),
]

