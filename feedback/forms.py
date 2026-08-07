from django import forms
from .models import FeedbackEntry

class FeedbackForm (forms.ModelForm):
    class Meta:
        model = FeedbackEntry
        fields = [
            'name',
            'email',
            'topic',
            'message',
            'rating',
        ]

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 20:
            raise forms.ValidationError("Message must be at least 20 characters.")
        return message


    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters.")
        return name