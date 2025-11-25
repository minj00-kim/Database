from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    nickname = forms.CharField(
        max_length=30,
        required=False,
        label="닉네임",
        widget=forms.TextInput(attrs={
            "class": "w-full border border-gray-300 rounded-lg px-3 py-2 text-sm",
            "placeholder": "닉네임 (선택)",
        }),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)

    def save(self, commit=True):
        user = super().save(commit)
        nickname = self.cleaned_data.get("nickname")
        if nickname:
            # Profile은 시그널로 자동 생성되니까 가져와서 닉네임만 세팅
            user.profile.nickname = nickname
            user.profile.save()
        return user
