from django import forms
from .models import UkrainianPassport, ForeignPassport


class UAPassportForm(forms.ModelForm):

    class Meta:
        model = UkrainianPassport
        fields = (
            'series',
            'number',
            'place_of_issue',
            'date_of_issue',
        )


class ForeignPassportForm(forms.ModelForm):

    class Meta:
        model = ForeignPassport
        fields = (
            'number',
            'authority',
            'date_of_expiry',
        )
