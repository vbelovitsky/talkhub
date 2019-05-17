from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control mr-sm-2'}))
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Body', 'class': 'form-control mr-sm-2'}))
    public = forms.BooleanField(required=False, label='Make post private:', widget=forms.CheckboxInput(attrs={'class': 'form-control mr-sm-2', 'name': 'public_check'}))

    class Meta:
        model = Post
        fields = (
            'title',
            'body',
        )


class PostEditForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control mr-sm-2'}))
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Body', 'class': 'form-control mr-sm-2'}))
    public = forms.BooleanField(required=False, label='Make post private:', widget=forms.CheckboxInput(
        attrs={'class': 'form-control mr-sm-2', 'name': 'public_check'}))

    class Meta:
        model = Post
        fields = (
            'title',
            'body',
        )


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control mr-sm-2'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control mr-sm-2'}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control mr-sm-2'}))
    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control mr-sm-2'}))
    last_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control mr-sm-2'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control mr-sm-2'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Enter password here', 'class': 'form-control mr-sm-2'}))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'form-control mr-sm-2'}))

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
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control mr-sm-2'}))
    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control mr-sm-2'}))
    last_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control mr-sm-2'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control mr-sm-2'}))

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
                                                            'class': 'textinputclass form-control mr-sm-2'}))

    class Meta:
        model = Comment
        fields = {'content'}
