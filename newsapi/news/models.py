from django.db import models

# Create your models here.
class Headline(models.Model):
  title = models.CharField(max_length=200)
  category = models.CharField(null=True, max_length=200)
  url = models.TextField()
  def __str__(self):
    return self.title