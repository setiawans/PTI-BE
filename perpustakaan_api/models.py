from django.db import models

# Create your models here.
class Perpustakaan(models.Model) :
    nama_perpustakaan = models.CharField(max_length = 100)
    alamat = models.CharField(max_length = 150)

class Genre(models.Model) :
    nama_genre = models.CharField(max_length = 50)

class Buku(models.Model) :
    judul = models.CharField(max_length = 100)
    pengarang = models.CharField(max_length = 100)
    genres = models.ManyToManyField(Genre)
    perpustakaan = models.ForeignKey(Perpustakaan, on_delete = models.CASCADE)
    