from rest_framework import serializers

from viewer.models import Movie, Genre


class MovieReadModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ["created"]


class MoviePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ["id", "created"]

    title = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(required=False)
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(),required=False)
    rating = serializers.IntegerField(required=False)
    released = serializers.DateField(required=False)
# or
class MovieCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)

    def validate(self, attrs): # validate data from multiple fields
        pass
    def validate_title(self): # validates something in title
        pass

