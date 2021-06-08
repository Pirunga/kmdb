from django.urls import path
from movies.views import (
    CriticCreateUpdateReviewView,
    ListCreateMovies,
    MovieRetrieveDestroyView,
    UserCreateUpdateCommentView,
)


urlpatterns = [
    path("movies/", ListCreateMovies.as_view()),
    path("movies/<int:movie_id>/", MovieRetrieveDestroyView.as_view()),
    path("movies/<int:movie_id>/review/", CriticCreateUpdateReviewView.as_view()),
    path("movies/<int:movie_id>/comments/", UserCreateUpdateCommentView.as_view()),
]
