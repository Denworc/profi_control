from django import forms

from user_profile.models import User
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


class DwellingUpdateForm(forms.ModelForm):

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
