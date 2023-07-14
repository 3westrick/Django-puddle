from django import forms
from .models import Conversation, ConvMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConvMessage
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }
