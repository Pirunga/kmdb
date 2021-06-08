from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.views import APIView
from movies.models import Comment, Criticism, Movie
from movies.serializers import CommentSerializer, CriticismSeriliazer, MovieSerializer
from movies.permissions import AdminPermission, CriticPermission, UserPermission
from movies.mixins import FieldLookUpMixin
import ipdb


class ListCreateMovies(FieldLookUpMixin, ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminPermission]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_fields = ["title"]


class MovieRetrieveDestroyView(RetrieveDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminPermission]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_url_kwarg = "movie_id"


class CriticCreateUpdateReviewView(CreateAPIView, UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CriticPermission]
    queryset = Criticism.objects.all()
    serializer_class = CriticismSeriliazer
    lookup_url_kwarg = "movie_id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie = get_object_or_404(Movie, pk=kwargs["movie_id"])
        critic = Criticism.objects.filter(movie=movie, critic=request.user)

        if critic:
            return Response(
                {"detail": "You already made this review."},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        critic = Criticism.objects.create(
            stars=request.data["stars"],
            review=request.data["review"],
            spoilers=request.data["spoilers"],
            critic=request.user,
            movie=movie,
        )

        serializer = CriticismSeriliazer(critic)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        movie = get_object_or_404(Movie, pk=kwargs["movie_id"])
        critic = get_object_or_404(Criticism, movie=movie, critic=request.user)

        critic.stars = request.data["stars"]
        critic.review = request.data["review"]
        critic.spoilers = request.data["spoilers"]

        critic.save()

        serializer = CriticismSeriliazer(critic)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class UserCreateUpdateCommentView(CreateAPIView, UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]
    queryset = Movie.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = "movie_id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie = get_object_or_404(Movie, pk=kwargs["movie_id"])
        comment = Comment.objects.create(
            comment=request.data["comment"],
            movie=movie,
            user=request.user,
        )

        serializer = CommentSerializer(comment)

        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        movie = get_object_or_404(Movie, pk=kwargs["movie_id"])
        comment = get_object_or_404(
            Comment, movie=movie, user=request.user, pk=request.data["comment_id"]
        )

        comment.comment = request.data["comment"]

        comment.save()

        serializer = CommentSerializer(comment)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
