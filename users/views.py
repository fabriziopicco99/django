from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Avatar
from .forms import AvatarForm
# from django.http import HttpResponse


# Create your views here.
def signup(request):
    print(request.method)
    form = UserCreationForm()
    if request.method == "GET":
        print("Enviadno formulario para crear usuario")
        return render(
        request,
        "signup.html",
        {"form": form, "name_butom": "signup"},
    )
    else:
        print("Creando usuario")
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        username = request.POST["username"]
        #Validamos las contraseñas
        if password1 != password2:
            return render(
                    request,
                    "signup.html",
                    {
                        "form": form,
                        "name_butom": "signup",
                        "notification": "Contraseñas no coinciden",
                    },
                )
        else:
            #Si las contraseñas coinciden, creamos el usuario
            try:
                #Intentamos crear el usuario
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)
                print("usuario creado")
                # return redirect("login")
                # redirect("Users")
                return redirect("/")
            except Exception as e:
                print(e)
                #Controlamos el error de que el usuario ya existe
                return render(
                    request,
                    "signup.html",
                    {
                        "form": form,
                        "name_butom": "signup",
                        "notification": "Username ya existe",
                    },
                )
    
def log_out(request):
    logout(request)
    return redirect("home")

def log_in(request):
    form = AuthenticationForm()
    if request.method == "GET":
        return render(
            request,
            "login.html",
            {"form": form, "name_butom": "Iniciar sesión"},
        )
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(
                request,
                "login.html",
                {
                    "form": form,
                    "name_butom": "Iniciar sesión",
                    "notification": "Usuario o contraseña incorrectos",
                },
            )
            
def view_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        print(f"user {user.pk}")
        avatar = Avatar.objects.filter(user_id=user.pk).first()
        print(f"avatar {avatar}")
        if avatar == None:
            print("No tiene avatar")
            avatar = Avatar(user=user, image="static/avatars/default.jpg", email='', name='', last_name='')
            avatar.save()
        print(user)
        print(avatar)
        return render(request, "view_user.html", {"user": user, "avatar": avatar})
    except Exception as e:
        print(e)

@login_required
def edit_user(request, pk):
    if request.method == "POST":
        try:
            # print(request.POST)
            #Busco el user que se va a actualizar
            print(f"pk {request}")
            user = get_object_or_404(User, pk=request.user.id)
            avatar = Avatar.objects.filter(user_id=user.pk).first()
            print(f"avatar {avatar}")
            print(f"user {user.pk}")
            #Obtengo los datos del formulario
            name = request.POST["name"]
            print(f"name {name}")
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            image = request.FILES.get("image")
            #Filtro los campos que se van a actualizar
            user_to_update = {}
            if image:
                user_to_update["image"] = image
            if name:
                user_to_update["name"] = name
            if last_name:
                user_to_update["last_name"] = last_name
            if email:
                user_to_update["email"] = email
            #Actualizo el User
            print(f"user_to_update {user_to_update}")
            user_update = AvatarForm(data=user_to_update, instance=avatar)
            user_update.save()
            return redirect("edit_user")
        except Exception as e:
            print("######################ERROR#######################")
            print(e)
            avatar = Avatar.objects.get(pk=pk, user=request.user)
            form = AvatarForm(instance=avatar)
            return render(
                request, "view_user.html", {"error": "Error al guardar el User","form": form}
            )
    else:
        user = User.objects.get(pk=request.user.pk)
        print(f"user {user.pk}")
        avatar = Avatar.objects.filter(user_id=user.pk).first()
        print(f"avatar {avatar}")
        if avatar == None:
            print("No tiene avatar")
            avatar = Avatar(user=user, image="static/avatars/default.jpg", email='', name='', last_name='')
            avatar.save()
        form = AvatarForm(instance=avatar)
        return render(request, "edit_user.html", {"form": form, "user": user, "avatar": avatar})