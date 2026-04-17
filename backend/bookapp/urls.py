from django.urls import path
from .views import add_book, list_books

urlpatterns = [
    path('add-book/', add_book),
    path('list-books/', list_books),
] 