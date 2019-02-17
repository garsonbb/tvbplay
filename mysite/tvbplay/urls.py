from django.urls import path, re_path
from . import views

urlpatterns = [
    path('aihuijia/',views.aihuijia),
    path('aihuijia/第<str:num>集/',views.player),
    path('collect',views.collect),
    path('',views.index),

]

