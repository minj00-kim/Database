# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # username, password1, password2 + email 필드까지 사용
        fields = UserCreationForm.Meta.fields + ('email',)
