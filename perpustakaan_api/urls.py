from django.urls import path
from .views import Part_Perpustakaan, Part_Perpustakaan_Id, Part_Perpustakaan_Buku_List, Part_Buku, Part_Buku_Id, Part_Genre, Part_Genre_Buku

urlpatterns = [
    path('perpustakaan', Part_Perpustakaan.as_view()),
    path('perpustakaan/<int:id>', Part_Perpustakaan_Id.as_view()),
    path('perpustakaan/<int:id>/buku', Part_Perpustakaan_Buku_List.as_view()),
    path('buku', Part_Buku.as_view()),
    path('buku/<int:id>', Part_Buku_Id.as_view()),
    path('genre', Part_Genre.as_view()),
    path('genre/<str:nama_genre>', Part_Genre_Buku.as_view())
]