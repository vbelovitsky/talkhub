from django import forms
from .models import *
from django.contrib.auth.models import User


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Body'}))

    class Meta:
        model = Post
        fields = (
            'title',
            'body',
        )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )



class PostEditForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Body'}))

    class Meta:
        model = Post
        fields = (
            'title',
            'body',
        )


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
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
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

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
