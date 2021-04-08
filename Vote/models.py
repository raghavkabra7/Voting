from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_detail(models.Model):
    usr = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=10, null=True)
    aadhar = models.CharField(max_length=12, null=True)
    DOB = models.CharField(max_length=15, null=True)
    id_proof = models.CharField(max_length=100, null=True)
    photo = models.FileField( null=True)
    def __str__(self):
        return self.name

class Party(models.Model):
    party_name = models.CharField(max_length=100, null=True)
    logo = models.FileField(null=True)

    def __str__(self):
        return self.party_name



class Nominance(models.Model):
    party_data =  models.ForeignKey(Party,on_delete = models.CASCADE,null=True)
    nomi_name = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    place = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.party_data.party_name + '-----' + self.nomi_name




