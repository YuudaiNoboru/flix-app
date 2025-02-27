from django.urls import path
from .views import MovieListCreatView, MovieRetrieveUpdateDestroyView


urlpatterns = [
    path('movies/', MovieListCreatView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(),
         name='movie-detail-view'),
]
