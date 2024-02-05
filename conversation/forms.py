from django import forms
from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model=ConversationMessage
        fields=[
        
        'content'
        ]
        widgets={
            'content':forms.Textarea(attrs={
                'class':'px-6 py-4 w-full rounded-xl border-2'
            })
        }