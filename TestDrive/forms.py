# from django.forms import ModelForm
from django import forms
from django.forms.formsets import BaseFormSet


class MessageForm(forms.Form):
    # sc_type = models.ForeignKey(to=Type, on_delete=models.CASCADE, null=True)
    # language = forms.ModelChoiceField(queryset=TypeForm)
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


class TypeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.sc_type = kwargs.pop('sc_type', None)
        super(TypeForm, self).__init__(*args, **kwargs)

        self.fields['name'] = forms.CharField(
            max_length=30,
            initial=self.sc_type.name,
            widget=forms.TextInput(attrs={
                'placeholder': 'SpeedCam code name',
            }))
        self.fields['number'] = forms.IntegerField(
            initial=self.sc_type.number,
            widget=forms.TextInput(attrs={
                'placeholder': 'Number',
            }))
        self.fields['description'] = forms.CharField(
            max_length=30,
            initial=self.sc_type.description,
            widget=forms.TextInput(attrs={
                'placeholder': 'SpeedCam description',
            }))


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
