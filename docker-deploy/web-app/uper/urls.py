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
    path('request_ride/', views.request_ride, name='request_ride'),
    path("edit_ride/", views.edit_ride, name="edit_ride"),    
    path('request_or_edit_ride_process/', views.request_or_edit_ride_process, name="request_or_edit_ride_process"),
    path('logout/',views.logout,name='logout'),
    path('driver_register/', views.driver_reg,name='driver_register'),
    path('driver_register_process/', views.driver_reg_process, name ='driver_register_process'),
    path('view_info/',views.view_info, name='view_info'),
    path('edit_driver/',TemplateView.as_view(template_name="uper/edit_driver.html"),name="edit_driver"),
    path("edit_driver_process/",views.edit_driver, name='edit_driver_process'),
    path("share_ride_search/",TemplateView.as_view(template_name="uper/share_ride_search.html"), name="share_ride_search"),
    path("shareride_search_result/", views.shareride_search_result, name="shareride_search_result"),
    path("join_shareride/",views.join_shareride,name="join_shareride"),
    path("driver_ride_search/",views.driver_ride_search, name="driver_ride_search"),
    path("take_order/",views.take_order,name="take_order"),
]

