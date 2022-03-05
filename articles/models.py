from django.db import models

# Create your models here.
class Article(models.Model):
    #every single Django models inherite from models.Model
    title = models.TextField()
    content = models.TextField()
    #after the model create run python3 manage.py makemigrations
    # then run python3 manage.py migrate