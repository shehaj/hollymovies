from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin
)

from api.serializers import MovieCreateModelSerializer, MovieReadModelSerializer, MoviePartialUpdateSerializer
from viewer.models import Movie


@api_view(["POST", "GET"])
def movies(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass


class MovieListCreateView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MovieCreateModelSerializer
        else:
            return MovieReadModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MovieDetailUpdateDeleteView(RetrieveModelMixin,
                                  UpdateModelMixin,
                                  DestroyModelMixin,
                                  GenericAPIView):
    queryset = Movie.objects.all()
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return MovieCreateModelSerializer
        elif self.request.method == "PATCH":
            return MoviePartialUpdateSerializer
        else:
            return MovieReadModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)