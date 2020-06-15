#myadmin Models are here

from django.db import models

# Admin Model
class Admin(models.Model):
    admin_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    email=models.EmailField(unique=True,blank=True)
    mobile=models.IntegerField(unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    photo=models.ImageField(upload_to="admin_photos/",blank=True)

    def __str__(self):
        return self.first_name