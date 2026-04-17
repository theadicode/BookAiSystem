from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

# FRONTEND PAGE
def home(request):
    books = Book.objects.all()
    return render(request, "bookapp/home.html", {"books": books})


# ADD BOOK + AI SUMMARY
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")

        # AI summary logic
        summary = f"This book titled '{title}' by {author} is a great read that explores important ideas and concepts."

        book = Book.objects.create(
            title=title,
            author=author,
            summary=summary
        )

        return JsonResponse({
            "message": "Book added successfully",
            "summary": summary
        })


# LIST BOOKS API
def list_books(request):
    books = Book.objects.all()

    data = []
    for b in books:
        data.append({
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "summary": b.summary
        })

    return JsonResponse(data, safe=False)