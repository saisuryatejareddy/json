from django.db import models

# Create your models here.
class Json(models.Model):
    JsonFile = models.FileField(blank=True,null=True)