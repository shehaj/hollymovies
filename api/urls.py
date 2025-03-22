from django.urls import path

from api.views import MovieListCreateView, MovieDetailUpdateDeleteView

urlpatterns = [
    path("movies", MovieListCreateView.as_view(), name='api-movies'),
    path("movies/<pk>", MovieDetailUpdateDeleteView.as_view(), name='api-movie'),
]