from django.urls import path
from . import views
urlpatterns = [
    path('',views.gohere),
    path('main', views.mainpage),
    path('createUser', views.create),
    path('login', views.login),
    path('travels', views.userpage),
    path('logout', views.logout),
    path('travels/add', views.addtrip),
    path('add_to_user_trips/<int:trip_id>', views.addtriptouser),
    path('home', views.homepage),
    path('addingAtrip', views.addingAtrip),
    path('destination/<int:trip_id>', views.trippage),
]