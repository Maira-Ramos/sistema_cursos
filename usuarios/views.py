from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Registrar novo usuário
def registrar_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso. Faça login!")
            return redirect("usuarios:login")
    else:
        form = UserCreationForm()

    return render(request, "usuarios/registro.html", {"form": form})


# Login
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Se for admin → pode redirecionar para painel/admin
            if user.is_superuser:
                return redirect("/admin/")

            # Usuário comum → home
            return redirect("home:index")   # ajuste para onde quiser

        messages.error(request, "Usuário ou senha incorretos.")

    return render(request, "usuarios/login.html")


# Logout
def logout_user(request):
    logout(request)
    return redirect("usuarios:login")
