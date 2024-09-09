from django.shortcuts import render


def register_view(request):

    return render(request, 'library/register.html')


def login_view(request):

    return render(request, 'library/login.html')


def update_user_view(request, user_id):

    return render(request, 'library/register.html')


def profile_user(request, user_id):

    return render(request, 'library/profile.html')


def delete_user(request, user_id):

    return render(request, 'library/profile.html')
