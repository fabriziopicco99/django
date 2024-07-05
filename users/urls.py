from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('view/<int:pk>', views.view_user, name='view_user'),
    path('edit/<int:pk>/', views.edit_user, name='edit_user'),
    # path('remove_user/<int:id>/', views.remove_user, name='remove_user'),
]