from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name =  models.CharField(max_length=60, null=False)
    password = models.CharField(max_length=45, null=False)
    show_name = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=45, null=True)
    phone = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=255, null=True)
    house_number = models.IntegerField(null=True)
    complement = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=100, null=True)
    CEP = models.CharField(max_length=20, null=True)
    CPF = models.CharField(max_length=12, null=True)
    active = models.BooleanField(null=True, default=True)
    type_organizer = models.BooleanField(null=True, default=False)
    type_participant = models.BooleanField(null=True, default=False)
    link = models.CharField(max_length=255, null=True)
    profile_picture = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user_name