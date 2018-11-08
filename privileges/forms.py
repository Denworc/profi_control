from django import forms

from user_profile.models import User
from .models import Quota


class QuotaCreateForm(forms.ModelForm):

    class Meta:
        model = Quota
        fields = (
            'type',
            'expire',
        )


class QuotaUpdateForm(forms.ModelForm):

    class Meta:
        model = Quota
        fields = (
            'type',
            'expire',
        )

    def __init__(self, pk, *args, **kwargs):
        super(QuotaUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        qouta = user.qoutas.get(id=1)
        self.fields['type'].initial = qouta.type
        self.fields['expire'].initial = qouta.expire
