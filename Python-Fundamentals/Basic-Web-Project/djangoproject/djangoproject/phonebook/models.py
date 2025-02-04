from django.db import models

# Create your models here.

#Use a built-in class models from django.db which will interact with the db
class Contact(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=14)

#Use below command to list any file which is in models.py
#python manage.py makemigrations
#Use below command to migrate it to the db
#python manage.py migrate
