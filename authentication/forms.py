from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import Form

from authentication.models import CustomUser


class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "password1", "password2"]


class CustomLoginForm(AuthenticationForm):
    pass


class CustomLogoutForm(Form):
    pass