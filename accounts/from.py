from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """
    회원가입을 위한 폼입니다.
    기본 UserCreationForm을 상속받아 username과 password를 처리합니다.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)  # 필요하다면 이메일 필드를 추가

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 폼 필드에 대한 추가적인 커스터마이징 (예: 스타일링)을 여기에 추가할 수 있습니다.