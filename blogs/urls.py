from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.BlogListView.as_view(), name='blog_list'),#Clase
    path('blog/create', views.create_blog, name='blog_create'),
    path('blog/edit/<int:pk>', views.edit_blog, name='blog_edit'),
    path('blog/delete/<int:pk>', views.delete_blog, name='blog_delete'),
    path('blog/view/<int:pk>', views.BlogDetailView.as_view(), name='blog_view'),#Clase
]