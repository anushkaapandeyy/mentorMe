from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("signup", views.sign_up, name="signup"),
    path("logout", views.logout_view, name="logout"),
    path("question/", views.question, name="question"),
    path("notification", views.notification, name="notification"),
    path("check", views.check, name="check"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("answer/<int:id>", views.answer, name="answer"),
    path("forum/<int:id>", views.forum, name="forum")
]