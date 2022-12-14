from django.db import models

# Create your models here.
class fruit_shop(models.Model):
    name=models.CharField(max_length=150)
    desc=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='picture')


    def __str__(self):
        return self.name