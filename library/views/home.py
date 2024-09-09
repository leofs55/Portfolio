from django.shortcuts import render
from library.models import Book
from itertools import groupby


def index(request):

    books = Book.objects.all().order_by('owner')
    books_per_owner = [(owner, list(books))
                       for owner, books in groupby(books, lambda x: x.owner)]
    context = {
        'books_per_owner': books_per_owner
    }
    return render(request, 'library/index.html', context)
