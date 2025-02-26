from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateLisstView, GenreRetrieveUpdateDestroyView
from actors.views import ActorListCreateView, ActorRetrieveUpdateDestroy
from movies.views import MovieListCreatView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateLisstView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(),
         name='genre-detail-view'),
    path('actors/', ActorListCreateView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroy.as_view(),
         name='actor-detail-view'),
    path('movies/', MovieListCreatView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(),
         name='movie-detail-view'),
]
