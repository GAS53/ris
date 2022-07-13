from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    field_order = [
        "username",
        "password1",
        "password2",
        "email",
        "first_name",
        "last_name",
        ]

    class Meta:
        model = get_user_model()
        fields = (
        "username",
        "email",
        "first_name",
        "last_name",
        )
        field_classes = {"username": UsernameField}