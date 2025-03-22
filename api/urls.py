from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import MovieListCreateView, MovieDetailUpdateDeleteView

urlpatterns = [
    path("movies", MovieListCreateView.as_view(), name='api-movies'),
    path("movies/<pk>", MovieDetailUpdateDeleteView.as_view(), name='api-movie'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]