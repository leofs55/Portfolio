# flake8: noqa
# type: ignore

from django.utils import timezone # type: ignore
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#descrição do livro: Nome, data de publicação, foto da capa, 
class Book(models.Model):
    title = models.CharField(max_length=99)
    author_book = models.CharField(max_length=99)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    pictures = models.ImageField(upload_to='library/pictures/%Y/%m/')
    show = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.author}: {self.content}'