from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_allowed_to_fetch = models.BooleanField(
        'Allowed to Fetch',
        default=False,
    )
    data_file_name = models.CharField(max_length=200,default="")
    updated_at = models.DateTimeField(auto_now=True)