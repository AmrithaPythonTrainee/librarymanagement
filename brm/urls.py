from . import views
from django.urls import path,include,re_path
from .views import *
urlpatterns = [
    path('',views.index,name="index"),
    path("loginandregister.html",index1),
    path('add-book/',addBookView),
    re_path('add-book/add',addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit",editBook),
    path("delete-book",deleteBookView),
    path("login/",user_login,name='login'),
    path("logout/",user_logout,name='logout'),
    path("register/",register,name='register'),
  ]
