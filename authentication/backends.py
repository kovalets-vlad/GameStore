# authentication/backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class NicknameBackend(BaseBackend):
    def authenticate(self, request, nickname=None, password=None, **kwargs):
        try:
            user = User.objects.get(nickname=nickname)
            if user.check_password(password):  # Перевірка хешованого паролю
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
