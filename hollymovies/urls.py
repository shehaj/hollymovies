"""
URL configuration for hollymovies project.

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

from authentication.models import CustomUser
from viewer.admin import MovieAdmin
from viewer.models import Genre, Movie
from viewer.views import (
    MovieListView,
    get_genres,
    hello,
    index,
    search,
    MovieCreateView,
    DirectorListView,
    DirectorCreateView,
    MoviesUpdateSimpleView,
    MovieDeleteView
)
from authentication.views import CustomRegistrationView, CustomLoginView, CustomLogoutView

# from viewer.views import *
# from authentication.views import *


admin.site.register(Genre)
admin.site.register(CustomUser)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", index, name="index"),
    # path("movies/", views.show_movies, name="movies"), # function based view
    # path("movies/", views.MoviesView.as_view(), name="movies"), # class-based view
    # path("movies/", views.MoviesTemplateView.as_view(), name="movies"), # class-based templateview
    path("movies/", MovieListView.as_view(), name="movies"),  # class-based listview
    path("index/<something>", hello),  # dynamic url
    path("index/search/", search),
    path("genres/", get_genres),
    path("movies/create/", MovieCreateView.as_view(), name='movie-create'),
    path("directors/create/", DirectorCreateView.as_view(), name='director-create'),
    path("directors/", DirectorListView.as_view(), name='directors'),
    path("movies/<pk>/edit/", MoviesUpdateSimpleView.as_view(), name='movie-update'),
    path("movies/<pk>/delete/", MovieDeleteView.as_view(), name='movie-delete'),
    path("auth/register/", CustomRegistrationView.as_view(), name='user-register'),
    path("auth/login/", CustomLoginView.as_view(), name='user-login'),
    path("auth/logout/", CustomLogoutView.as_view(), name='user-logout'),
    path("api/", include("api.urls"))
]
