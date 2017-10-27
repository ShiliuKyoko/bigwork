from django import forms
from django.core.exceptions import ValidationError

def words_validator(content):
    if len(content) < 5:
        raise ValidationError('words NOT ENOUGH!')

def commnet_validator(content):
    if 'fuck' in content:
        raise ValidationError('Do not use that word!')

class CommentForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(
    widget=forms.Textarea(),
        error_messages={
            'required':'wow,such words'
            },
    validators=[words_validator, commnet_validator]
    )

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
