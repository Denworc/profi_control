from django import forms
from .models import Insurance


class InsuranceCreateForm(forms.ModelForm):

    class Meta:
        model = Insurance
        fields = (
            'type',
            'start_on',
            'expire',
            'scan_copy',
        )
