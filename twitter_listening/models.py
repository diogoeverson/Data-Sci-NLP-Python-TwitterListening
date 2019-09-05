#from django.db import models
from djongo import models


# Create your models here.
class tweets(models.Model):
    _id = models.ObjectIdField()
    created_at = models.DateTimeField()
    id_str = models.CharField(max_length=500)
    text = models.TextField()
