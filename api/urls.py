from django.urls import path 
from . import views

urlpatterns = [
    path('',views.get_api,name="get_api"),
    path('message/',views.post_message,name="post_message"),
]
