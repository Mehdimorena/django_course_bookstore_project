from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        #fields = UserCreationForm.Meta.fields + ('age',)
        # username + age + password1 + password2   بصورت خودکار اینا رو نشون میده
        fields = ('username', 'age', 'email', ) # میام تعیین میکنم چیا رو از کاربر دریافت کنه


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        #fields = UserChangeForm.Meta.fields
        fields = ('username', 'age', 'email', )
