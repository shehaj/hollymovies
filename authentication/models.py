from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        db_table = "custom_user"
