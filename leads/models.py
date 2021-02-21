from django.db import models
from django.contrib.auth.models import AbstractUser

#User = get_user_model()

# Create your models here.
class User(AbstractUser):
    #cellphone_number = models.CharField(max_length=15)
    pass

class Lead(models.Model):
    SOURCE_CHOICES = (
        ('YT','Youtube'),
        ('GOOGLE','Google'),
        ('NL','NewsLetter')
    )
    # we are required to require the kind of the field
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0) # cant be less than 0

    phoned = models.BooleanField(default=False)
    sources = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    profile_picture = models.ImageField(blank=True,null=True)
    special_files = models.FileField(blank=True,null=True)

    # fkeys
    agent = models.ForeignKey('SalesAgents', on_delete = models.CASCADE)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)
class SalesAgents(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #we dont need to have 1st and last name because we have them on the abstract user
    #first_name = models.CharField(max_length=20)
    #last_name = models.CharField(max_length=20)
    def __str__(self):
        return self.user.email


