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


class InsuranceUpdateForm(forms.ModelForm):

    class Meta:
        model = Insurance
        fields = (
            'type',
            'start_on',
            'expire',
            'scan_copy',
        )

    def __init__(self, pk, *args, **kwargs):
        super(DwellingUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        dwelling = user.dwellings.get(id=1)
        self.fields['address'].initial = dwelling.address
        self.fields['landlord_name'].initial = dwelling.landlord_name
        self.fields['neighbor_name'].initial = dwelling.neighbor_name
        self.fields['start_on'].initial = dwelling.start_on
        self.fields['expire'].initial = dwelling.expire
        self.fields['end_date'].initial = dwelling.end_date
