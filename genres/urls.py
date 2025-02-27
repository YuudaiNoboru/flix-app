from django.urls import path
from .views import GenreCreateLisstView, GenreRetrieveUpdateDestroyView


urlpatterns = [
    path('genres/', GenreCreateLisstView.as_view(), name='movie-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(),
         name='movie-detail-view'),
]
