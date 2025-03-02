from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from review.models import Review
from review.serializer import ReviewSerializers


class ReviewListeCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
