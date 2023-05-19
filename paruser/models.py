
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    profile_role = models.CharField(max_length=400, blank=True, null=True,)
    profile_company_created = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed