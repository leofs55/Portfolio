from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),

    # books (CRUD)
    path('user/book/create/',
         views.book_create, name='create'),
    path('user/book/<int:id_book>/details',
         views.book_details, name='details'),
    path('user/book/<int:id_book>/update',
         views.book_update, name='update'),
    path('user/book/<int:id_book>/delete',
         views.book_delete, name='delete'),

    # user - não acessar por enquanto

    path('user/login/',
         views.login_view, name='login'),
    path('user/register/',
         views.register_view, name='register'),
    path('user/<int:user_id>/update/',
         views.update_user_view, name='update-user'),
    path('user/<int:user_id>/details/',
         views.profile_user, name='profile'),

]
