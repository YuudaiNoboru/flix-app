from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        raise NotImplementedError('Falta implementar a função.')

    def validate_release_data(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode \
                                              ser anterior a 1990.')
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não deve ser maior que \
                                              200 caracteres.')
        return value
