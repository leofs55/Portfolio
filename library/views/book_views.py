from django.shortcuts import render


def book_details(request, id_book):

    return render(request, 'library/details.html')


def book_create(request):

    return render(request, 'library/details.html')


def book_delete(request, id_book):

    return render(request, 'library/details.html')


def book_update(request, id_book):

    return render(request, 'library/details.html')
