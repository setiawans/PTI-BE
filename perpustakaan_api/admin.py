from django.contrib import admin
from .models import Perpustakaan, Buku, Genre
# Register your models here.
admin.site.register(Perpustakaan)
admin.site.register(Buku)
admin.site.register(Genre)