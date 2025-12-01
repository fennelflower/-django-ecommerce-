from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmailValidationForm(UserCreationForm):
    # 添加一个必须填写的邮箱字段
    email = forms.EmailField(label='电子邮箱', required=True, help_text='我们需要您的邮箱来发送订单确认信')

    class Meta:
        model = User
        # 指定表单里显示哪些字段：用户名、邮箱、(密码是默认自带的)
        fields = ("username", "email")