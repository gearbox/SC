# from django.forms import ModelForm
from django import forms
from django.forms.formsets import BaseFormSet

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['first_name'] = forms.CharField(
            required=False,
            max_length=30,
            initial=self.user.first_name,
            label='First Name',
            widget=forms.TextInput(attrs={
                'placeholder': 'First Name'
            })
        )
        self.fields['last_name'] = forms.CharField(
            required=False,
            max_length=30,
            initial=self.user.last_name,
            widget=forms.TextInput(attrs={
                'placeholder': 'Last Name'
            })
        )


class MessageForm(forms.Form):
    # language = forms.ModelChoiceField(queryset=SCTypeForm)
    language = forms.CharField()
    message = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Text of the voice message'}),
        required=False)
    audio_file_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Filename'}),
        required=False)
    image_file_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Filename'}),
        required=False)
    # class Meta:
    #     model = Message
    #     fields = ['language', 'message', 'audio_file_name', 'image_file_name']


class SCTypeForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'SpeedCam code name',
        })
    )
    number = forms.IntegerField(
        localize=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'SpeedCam type number',
        })
    )
    description = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'SpeedCam description',
        })
    )


class BaseMessageFormset(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return

        messages = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                message = form.cleaned_data['message']

                # Check that no two links have the same anchor or URL
                if message:
                    if message in messages:
                        duplicates = True
                    messages.append(message)

                if duplicates:
                    raise forms.ValidationError(
                        'Messages should be unique',
                        code='duplicate_messages'
                    )

                # Check that all links have both an anchor and URL
                '''if url and not anchor:
                    raise forms.ValidationError(
                        'All links must have an anchor.',
                        code='missing_anchor'
                    )
                elif anchor and not url:
                    raise forms.ValidationError(
                        'All links must have a URL.',
                        code='missing_URL'
                    )'''
