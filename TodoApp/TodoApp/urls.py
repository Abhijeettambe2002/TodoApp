"""
URL configuration for TodoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("events.urls")),
    path("", views.user, name="user"),
    path("main_page/", views.main_page, name="main_page"),
    path("login_page/", views.login_page, name="login_page"),
    path("logout_page/", views.logout_page, name="logout_page"),
    path("add_event/", views.add_event, name="add_event"),
    path("delete_event/<int:event_id>/", views.delete_event, name="delete_event"),
    path("update_event/<int:event_id>/", views.update_event, name="update_event"),
    path("event_detail/<int:event_id>/", views.event_detail, name="event_detail"),
]
