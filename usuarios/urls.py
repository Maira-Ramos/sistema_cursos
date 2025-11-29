from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("", views.login_user, name="login"),  # rota principal
    path("login/", views.login_user, name="login"),
    path("registro/", views.registrar_usuario, name="registro"),
    path("logout/", views.logout_user, name="logout"),
]
