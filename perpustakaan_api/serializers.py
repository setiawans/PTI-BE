from rest_framework import serializers
from .models import Perpustakaan, Buku, Genre

class Perpustakaan_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Perpustakaan
        fields = '__all__'

class Genre_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class PerpustakaanField(serializers.PrimaryKeyRelatedField):
    def to_internal_value(self, data):
        try:
            data = int(data)
        except ValueError:
            pass
        try:
            if isinstance(data, str):
                return Perpustakaan.objects.get(nama_perpustakaan=data)
            elif isinstance(data, int):
                return super().to_internal_value(str(data))
        except Perpustakaan.DoesNotExist:
            raise serializers.ValidationError('Perpustakaan dengan nama atau ID tersebut tidak ada')

class GenreField(serializers.PrimaryKeyRelatedField):
    def to_internal_value(self, data):
        try:
            data = int(data)
        except ValueError:
            pass
        try:
            if isinstance(data, str):
                return Genre.objects.get(nama_genre=data)
            elif isinstance(data, int):
                return super().to_internal_value(str(data))
        except Genre.DoesNotExist:
            raise serializers.ValidationError('Genre dengan nama atau ID tersebut tidak ada')


class Buku_Serializer(serializers.ModelSerializer):
    perpustakaan = PerpustakaanField(write_only = True, queryset=Perpustakaan.objects.all())
    genres = GenreField(write_only = True, many=True, queryset=Genre.objects.all())
    perpustakaan_info = Perpustakaan_Serializer(source='perpustakaan', read_only=True)
    genres_info = Genre_Serializer(source='genres', many=True, read_only=True)

    class Meta:
        model = Buku
        fields = ('id', 'judul', 'pengarang', 'perpustakaan', 'genres', 'perpustakaan_info', 'genres_info')