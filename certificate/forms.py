from django import forms
from .models import Interview


class InterviewCreateForm(forms.ModelForm):

    class Meta:
        model = Interview
        fields = (
            'start_on',
            'type',
            'result',
        )
