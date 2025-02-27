from django.urls import path
from .views import ActorListCreateView, ActorRetrieveUpdateDestroy


urlpatterns = [
    path('actors/', ActorListCreateView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroy.as_view(),
         name='actor-detail-view'),
]
