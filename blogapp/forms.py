from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
        )


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
        )


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label='', attrs={'placeholder': 'Username'})
    first_name = forms.CharField(max_length=20, label='', attrs={'placeholder': 'First name'})
    last_name = forms.CharField(max_length=20, label='', attrs={'placeholder': 'Last name'})
    email = forms.EmailField(label='', attrs={'placeholder': 'Email'})
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Enter password here'}))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords are not equal')
        return confirm_password


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )


class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=1000,
                              label="",
                              widget=forms.TextInput(attrs={'placeholder': 'Comment here',
                                                            'id': 'textinput',
                                                            'class': 'textinputclass'}))

    class Meta:
        model = Comment
        fields = {'content'}
