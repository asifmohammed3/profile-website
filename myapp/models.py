from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100, default='')
    role1 = models.CharField(max_length=100, default='')
    role2 = models.CharField(max_length=100, default='')
    whatsappLink = models.CharField(max_length=500, default='')
    facebookLink = models.CharField(max_length=500, default='')
    githubLink = models.CharField(max_length=500, default='')
    instagramLink = models.CharField(max_length=500, default='')
    linkedinLink = models.CharField(max_length=500, default='')
