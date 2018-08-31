from django.urls import path
from accounts import views





urlpatterns = [

    path("reqister/", views.signup_sponsor, name="reqister"),

]



