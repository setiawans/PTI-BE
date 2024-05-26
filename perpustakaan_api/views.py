from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Perpustakaan, Buku, Genre
from .serializers import Perpustakaan_Serializer, Buku_Serializer, Genre_Serializer

# Create your views here.
class Part_Perpustakaan(APIView) :
    def get(self, request) :
        item = Perpustakaan.objects.all()
        serializer = Perpustakaan_Serializer(item, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request) :
        serializer = Perpustakaan_Serializer(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Part_Perpustakaan_Id(APIView) :
    def get(self, request, id) :
        item = get_object_or_404(Perpustakaan, id = id)
        serializer = Perpustakaan_Serializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id) :
        item = get_object_or_404(Perpustakaan, id = id)
        serializer = Perpustakaan_Serializer(item, data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id) :
        item = get_object_or_404(Perpustakaan, id = id)
        item.delete()
        return Response({'message' : 'Perpustakaan berhasil dihapus'}, status=status.HTTP_200_OK)

class Part_Perpustakaan_Buku_List(APIView) :
    def get(self, request, id) :
        perpustakaan = get_object_or_404(Perpustakaan, id = id)
        buku = Buku.objects.filter(perpustakaan = perpustakaan)
        serializer = Buku_Serializer(buku, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Part_Buku(APIView) :
    def get(self, request) :
        item = Buku.objects.all()
        serializer = Buku_Serializer(item, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request) :
        serializer = Buku_Serializer(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Part_Buku_Id(APIView) :
    def put(self, request, id) :
        item = get_object_or_404(Buku, id = id)
        serializer = Buku_Serializer(item, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id) :
        item = get_object_or_404(Buku, id = id)
        item.delete()
        return Response({'message' : 'Buku berhasil dihapus'}, status=status.HTTP_200_OK)

class Part_Genre(APIView) :
    def get(self, request) :
        item = Genre.objects.all()
        serializer = Genre_Serializer(item, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request) :
        serializer = Genre_Serializer(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Part_Genre_Buku(APIView) :
    def get(self, request, nama_genre) :
        genre = get_object_or_404(Genre, nama_genre__iexact=nama_genre)
        buku = Buku.objects.filter(genres = genre)
        serializer = Buku_Serializer(buku, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        