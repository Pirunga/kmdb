from django.contrib.auth.models import User
from rest_framework import serializers

from movies.models import Genre, Movie, Criticism, Comment


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    class Meta:
        model = Genre
        fields = ["id", "name"]


class UserOutPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]


class CriticismSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Criticism
        fields = ["id", "critic", "stars", "review", "spoilers"]

    stars = serializers.IntegerField(min_value=1, max_value=10)
    critic = UserOutPutSerializer(read_only=True)

    def create(self, validated_data):
        critic = Criticism.objects.get_or_create(
            stars=validated_data["stars"],
            review=validated_data["review"],
            spoiler=validated_data["spoiler"],
        )[0]

        movie = Movie.objects.get_object_or_404(id=validated_data["movie_id"])

        movie.criticism_set.add(critic)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "comment"]

    user = UserOutPutSerializer(read_only=True)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "genres",
            "launch",
            "classification",
            "synopsis",
            "criticism_set",
            "comment_set",
        ]

    def create(self, validated_data):
        movie = Movie.objects.get_or_create(
            title=validated_data["title"],
            duration=validated_data["duration"],
            launch=validated_data["launch"],
            classification=validated_data["classification"],
            synopsis=validated_data["synopsis"],
        )[0]

        genres = validated_data["genres"]

        for genre in genres:
            genre_created = Genre.objects.get_or_create(**genre)[0]
            movie.genres.add(genre_created)

        return movie

    genres = GenreSerializer(many=True)
    criticism_set = CriticismSeriliazer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
