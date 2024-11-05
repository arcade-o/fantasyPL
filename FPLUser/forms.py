from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import FPLUser

class FPLUserCreationForm(UserCreationForm):

    class Meta:
        model = FPLUser
        fields = ("email",)

class FPLUserChangeForm(UserChangeForm):

    class Meta:
        model = FPLUser
        fields = ("email",)

        