from django.urls import path,include
from . import views


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/",views.RegisterView.as_view(),name="sign_up")
]