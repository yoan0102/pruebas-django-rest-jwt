from django.urls import path


from . import views


urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('login/', views.LoginView.as_view()),
]
