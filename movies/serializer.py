from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(rate=Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None

    def validate_release_data(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode \
                                              ser anterior a 1900S.')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não deve ser maior que \
                                              500 caracteres.')
        return value
