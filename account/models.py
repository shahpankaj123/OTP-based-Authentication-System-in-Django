from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Auth_token=models.CharField(max_length=100)
    verifiedid=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

# Create your models here.
