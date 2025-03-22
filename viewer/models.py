from django.db import models
from django.db.models import (
    CharField,
    IntegerField,
    DateField,
    TextField,
    DateTimeField,
    ForeignKey, DO_NOTHING
)

class Genre(models.Model):
    name = CharField(max_length=128)  # VARCHAR 128

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = CharField(max_length=100)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)
    genre = ForeignKey("Genre", on_delete=DO_NOTHING)

    def __repr__(self):
        return f"{self.title} - {self.released}"

    def __str__(self):
        return f"{self.title} - {self.released}"


class Director(models.Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)

    def __repr__(self):
        return f"{self.first_name} - {self.last_name}"

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"