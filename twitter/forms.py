from django import forms

from twitter import models


class TweetForm(forms.ModelForm):
    class Meta:
        model = models.Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea()
        }