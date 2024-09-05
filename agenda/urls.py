from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # contact (CRUD)
    path('contact/<int:contact_id>/details/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    # user
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),  # type:ignore
]

#     path('contact/create/', views.contact, name='contact'),
#     path('contact/<int:contact_id>/update/', views.contact, name='contact'),
#     path('contact/<int:contact_id>/delete/', views.contact, name='contact'),
