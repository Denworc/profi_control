from django import forms
from .models import Dwelling


class DwellingCreateForm(forms.ModelForm):

    class Meta:
        model = Dwelling
        fields = (
            'address',
            'landlord_name',
            'neighbor_name',
            'start_on',
            'expire',
            'end_date',
        )
