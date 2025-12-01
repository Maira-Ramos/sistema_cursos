from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Código secreto que identifica professores
CODIGO_PROFESSOR = "PROF123"  # substitua pelo código real

# -----------------------------
# Registrar novo usuário
# -----------------------------
def registrar_usuario(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Codifica a senha corretamente
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Fallback seguro: cria grupos se não existirem
            grupo_aluno, _ = Group.objects.get_or_create(name="Aluno")
            grupo_professor, _ = Group.objects.get_or_create(name="Professor")

            # Verifica se é professor ou aluno pelo código secreto
            codigo = form.cleaned_data.get("codigo_professor", "").upper().strip()
            if codigo == CODIGO_PROFESSOR:
                user.groups.add(grupo_professor)
                grupo_nome = "Professor"
            else:
                user.groups.add(grupo_aluno)
                grupo_nome = "Aluno"

            messages.success(
                request,
                f"Conta criada com sucesso e adicionada ao grupo {grupo_nome}. Faça login!"
            )
            return redirect("usuarios:login")
    else:
        form = CustomUserCreationForm()

    return render(request, "usuarios/registro.html", {"form": form})

# -----------------------------
# Login
# -----------------------------
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("usuarios:home")  # Redireciona para a home
            else:
                messages.error(request, "Usuário inativo.")
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, "usuarios/login.html")

# -----------------------------
# Logout
# -----------------------------
def logout_user(request):
    logout(request)
    return redirect("usuarios:login")

# -----------------------------
# Home / Dashboard
# -----------------------------
@login_required
def home(request):
    user = request.user

    # Garante que os grupos existam
    grupo_aluno, _ = Group.objects.get_or_create(name="Aluno")
    grupo_professor, _ = Group.objects.get_or_create(name="Professor")

    # Verifica se usuário pertence aos grupos
    is_professor = grupo_professor in user.groups.all()
    is_aluno = grupo_aluno in user.groups.all()

    # DEBUG opcional: imprime no terminal
    print(f"Usuário: {user.username} | Professor: {is_professor} | Aluno: {is_aluno}")

    return render(request, "home.html", {
        "is_professor": is_professor,
        "is_aluno": is_aluno,
    })

# -----------------------------
# Perfil do Usuário
# -----------------------------
@login_required
def perfil_usuario(request):
    user = request.user

    # Lógica de verificação de grupo (replicada para definir o papel)
    try:
        grupo_professor = Group.objects.get(name="Professor")
        is_professor = grupo_professor in user.groups.all()
    except Group.DoesNotExist:
        # Fallback seguro se o grupo não existir
        is_professor = False

    context = {
        "usuario": user,
        "is_professor": is_professor,
    }

    # Você precisa criar o template 'perfil.html'
    return render(request, "perfil.html", context)