from django import forms
from .models import Post, Comment, Profile
from django.contrib.auth.models import User


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Title', 'data-role': "input", 'data-prepend': "<span class='mif-description'>", 'autocomplete': 'off'
            }))
    body = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Body', 'data-role': "textarea"}))
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
        attrs={'placeholder': 'Title', 'data-role': "materialinput", 'data-icon': "<span class='mif-pencil'>", 
            'data-label': "Enter title here", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan", 'autocomplete': 'off'
            }))
    body = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Body', 'data-role': "textarea", 'autocomplete': 'off'
            }))
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
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan", 'autocomplete': 'off'
            }))
    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(
        attrs={'placeholder': 'First name', 'data-role': "materialinput", 'data-icon': "<span class='mif-info'>", 
            'data-label': "First name", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan", 'autocomplete': 'off'
            }))
    last_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Last name', 'data-role': "materialinput",
            'data-label': "Last name", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'autocomplete': 'off'
            }))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'placeholder': 'Enter your email', 'data-role': "materialinput", 'data-icon': "<span class='mif-envelop'>", 
            'data-label': "User email", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan", 'autocomplete': 'off'
        }))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter password here', 'data-role': "materialinput", 'data-icon': "<span class='mif-lock'>", 
            'data-label': "Enter password here", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan", 'autocomplete': 'off'
            }))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm password', 'data-role': "materialinput",
            'data-label': "Confirm password", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'autocomplete': 'off'
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
        attrs={'placeholder': 'Username', 'data-role': "materialinput", 'data-icon': "<span class='mif-user'>", 
            'data-label': "Enter username here", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan", 'autocomplete': 'off'
            }))
    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(
        attrs={'placeholder': 'First name', 'data-role': "materialinput", 'data-icon': "<span class='mif-contacts-mail'>", 
            'data-label': "Enter first name here", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan", 'autocomplete': 'off'
            }))
    last_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Last name', 'data-role': "materialinput", 'data-icon': "<span class='mif-contacts-mail'>", 
            'data-label': "Enter last name here", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan", 'autocomplete': 'off'
            }))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'data-role': "materialinput", 'data-icon': "<span class='mif-mail'>", 
            'data-label': "Enter email here", 'data-cls-line': "bg-cyan", 'data-cls-label': "fg-cyan",
            'data-cls-informer': "fg-lightCyan", 'data-cls-icon': "fg-darkCyan", 'autocomplete': 'off'
            }))

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
                                                            'id': 'textinput'}))

    class Meta:
        model = Comment
        fields = {'content'}


class ProfileForm(forms.ModelForm):
    image = forms.FileField(required=False, widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = {'image'}
