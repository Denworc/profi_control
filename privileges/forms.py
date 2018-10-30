from django import forms
from .models import Quota


class QuotaCreateForm(forms.ModelForm):

    class Meta:
        model = Quota
        fields = (
            'type',
            'expire',
        )
