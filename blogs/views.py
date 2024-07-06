from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .models import Blog
from .form import BlogForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "home.html")


class BlogListView(ListView):
    model = Blog
    template_name = "list_blogs.html"
    context_object_name = "blogs"

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get("title")
        
        if title:
            queryset = queryset.filter(title=title)

        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = "view_blog.html"
    context_object_name = "blog"


@login_required
def create_blog(request):
    if request.method == "POST":
        try:
            # Busco los datos del formulario
            title = request.POST["title"]
            description = request.POST["description"]
            image = request.FILES["image"]
            user = request.user
            # Creo el blog
            blog = Blog(title=title, description=description, image=image, user=user)
            blog.save()
            return redirect("blog_list")
        except Exception as e:
            # Capturo el error y muestro un mensaje de error
            print(e)
            form = BlogForm()
            return render(
                request,
                "create_blog.html",
                {"error": "Error al guardar el blog", "form": form},
            )
    else:
        form = BlogForm()
        return render(request, "create_blog.html", {"form": form})


@login_required
def edit_blog(request, pk):
    if request.method == "POST":
        try:
            # print(request.POST)
            # Busco el blog que se va a actualizar
            blog = get_object_or_404(Blog, pk=pk, user=request.user)
            # Obtengo los datos del formulario
            title = request.POST["title"]
            description = request.POST["description"]
            image = request.FILES.get("image")
            # Filtro los campos que se van a actualizar
            blog_to_update = {}
            files_to_update = {}
            if image:
                files_to_update["image"] = image
            if title:
                blog_to_update["title"] = title
            if description:
                blog_to_update["description"] = description
            # Actualizo el blog
            blog_update = BlogForm(blog_to_update, files=files_to_update, instance=blog)
            blog_update.save()
            return redirect("blog_list")
        except Exception as e:
            print("######################ERROR#######################")
            print(e)
            blog = Blog.objects.get(pk=pk, user=request.user)
            form = BlogForm(instance=blog)
            return render(
                request,
                "edit_blog.html",
                {"error": "Error al guardar el blog", "form": form},
            )
    else:
        # Obtengo el blog que se va a editar
        blog = Blog.objects.get(pk=pk, user=request.user)
        # Creo el formulario con los datos del blog
        form = BlogForm(instance=blog)
        return render(request, "edit_blog.html", {"form": form})


@login_required
def delete_blog(request, pk):
    # Obtengo el blog que se va a eliminar
    blog = Blog.objects.get(pk=pk, user=request.user)
    # Elimino la imagen asociada al blog
    if blog.image:
        blog.image.delete()
    # Elimino el blog
    blog.delete()
    return redirect("blog_list")
