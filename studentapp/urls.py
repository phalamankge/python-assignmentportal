from django.urls import path,include
from . import views



urlpatterns = [
    
    path("register/", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('', views.student_form,name='student_insert'), 
    path('<int:id>/', views.student_form,name='student_update'), 
    path('delete/<int:id>/',views.student_delete,name='student_delete'),
    path('list/',views.student_list,name='student_list') 
]