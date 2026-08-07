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