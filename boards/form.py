from django import forms
from .models import Topic

class add_new_topic(forms.ModelForm):

    message =forms.CharField(widget=forms.Textarea , max_length=4000 , help_text=)

    class Meta:
        model = Topic
        fields = ['subject' , 'message'] 