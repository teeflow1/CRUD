from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout_user', views.logout_user, name = 'logout'),
    path('register_user', views.register_user, name = 'register'),
    path('detail_record/<int:pk>', views.detail_record, name = 'record'),
    path('delete_record/<int:pk>', views.delete_record, name = 'delete'),
    path('add_record', views.add_record, name = 'add_record'),
    path('update_user(/<int:pk>', views.update_user, name = 'update'),
]




