from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'first_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
