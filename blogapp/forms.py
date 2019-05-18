from django import forms
from .models import Post, Comment, Profile
from django.contrib.auth.models import User


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Title', 'class': 'form-control mr-sm-2'}))
    body = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Body', 'class': 'form-control mr-sm-2'}))
    private = forms.BooleanField(required=False, label='Make post private:', widget=forms.CheckboxInput(
        attrs={'class': 'form-control mr-sm-2'}))

    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'private'
        )


class PostEditForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Title', 'class': 'form-control mr-sm-2'}))
    body = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Body', 'class': 'form-control mr-sm-2'}))
    private = forms.BooleanField(required=False, label='Make post private:', widget=forms.CheckboxInput(
        attrs={'class': 'form-control mr-sm-2'}))

    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'private'
        )


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control mr-sm-2'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control mr-sm-2'}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'data-role': "materialinput", 'data-icon': "<span class='mif-user-plus'>", 
            'data-label': "Username", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan"
            }))
    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(
        attrs={'placeholder': 'First name', 'data-role': "materialinput", 'data-icon': "<span class='mif-info'>", 
            'data-label': "First name", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan"
            }))
    last_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Last name', 'data-role': "materialinput",
            'data-label': "Last name", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan"
            }))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'placeholder': 'Enter your email', 'data-role': "materialinput", 'data-icon': "<span class='mif-envelop'>", 
            'data-label': "User email", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan"
        }))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter password here', 'data-role': "materialinput", 'data-icon': "<span class='mif-lock'>", 
            'data-label': "Enter password here", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan"
            }))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm password', 'data-role': "materialinput",
            'data-label': "Confirm password", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan"
            }))

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
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control mr-sm-2'}))
    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(
        attrs={'placeholder': 'First name', 'class': 'form-control mr-sm-2'}))
    last_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Last name', 'class': 'form-control mr-sm-2'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': 'form-control mr-sm-2'}))

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


class ProfileForm(forms.ModelForm):
    image = forms.FileField(required=False, widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = {'image'}
