from django import forms
from .models import UkrainianPassport, ForeignPassport, Visa, PersonalID


class UAPassportForm(forms.ModelForm):

    class Meta:
        model = UkrainianPassport
        fields = (
            'series',
            'number',
            'place_of_issue',
            'date_of_issue',
            'first_page',
            'second_page',
            'registration',
        )


class ForeignPassportForm(forms.ModelForm):

    class Meta:
        model = ForeignPassport
        fields = (
            'number',
            'authority',
            'date_of_expiry',
            'first_page',
        )


class VisaCreateForm(forms.ModelForm):

    class Meta:
        model = Visa
        fields = (
            'first_date',
            'prediction_date',
            'start_on',
            'expire',
            'visa_scan',
        )


class PersonalIDCreateForm(forms.ModelForm):

    class Meta:
        model = PersonalID
        fields = (
            'personal_id',
            'scan_id',
        )
