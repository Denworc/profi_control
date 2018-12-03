from django import forms

from user_profile.models import User
from .models import Insurance


class InsuranceCreateForm(forms.ModelForm):

    class Meta:
        model = Insurance
        fields = (
            'pay_date',
            'type',
            'start_on',
            'expire',
            'scan_copy',
        )


class InsuranceUpdateForm(forms.ModelForm):

    class Meta:
        model = Insurance
        fields = (
            'pay_date',
            'type',
            'start_on',
            'expire',
            'scan_copy',
        )

    def __init__(self, pk, *args, **kwargs):
        super(InsuranceUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        insurance = user.insurances.get(id=1)
        self.fields['type'].initial = insurance.type
        self.fields['start_on'].initial = insurance.start_on
        self.fields['expire'].initial = insurance.expire
        self.fields['scan_copy'].initial = insurance.scan_copy
