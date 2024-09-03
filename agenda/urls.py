from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # contact (CRUD)
    path('contact/<int:contact_id>/details/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
]

#     path('contact/create/', views.contact, name='contact'),
#     path('contact/<int:contact_id>/update/', views.contact, name='contact'),
#     path('contact/<int:contact_id>/delete/', views.contact, name='contact'),
