from django.core.exceptions import ValidationError
from django.forms import (
    Form,
    CharField,
    IntegerField,
    DateField,
    CharField,
    Textarea,
    ModelChoiceField, ModelForm
)
from datetime import date

from viewer.models import Genre, Movie, Director


def date_validator(value):
    if value < date(year=1970, month=1, day=1):
        raise ValidationError('Date cannot be older than 1970-01-01')
    return value

class MovieForm(Form):
    title = CharField(max_length=100)
    rating = IntegerField(min_value=1, max_value=10)
    released = DateField(validators=[date_validator])
    description = CharField(widget=Textarea)
    genre = ModelChoiceField(queryset=Genre.objects)

    def clean_title(self):
        return self.cleaned_data["title"].capitalize()

    def clean_rating(self):
        if 3 <= self.cleaned_data["rating"] <= 5:
            raise ValidationError("The rating cannot be between 3 and 5")
        return self.cleaned_data["rating"]

    def clean(self):
        if self.cleaned_data["genre"].name == 'action' and self.cleaned_data["rating"] >= 8:
            raise ValidationError("Action movies cannot be that good")
        return super().clean()


class MovieModelForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    rating = IntegerField(min_value=1, max_value=10)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def print_hello(self):
        return "Hello"



class DirectorModelForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
