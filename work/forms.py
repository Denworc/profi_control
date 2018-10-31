from django import forms
from .models import (
    Dismissal,
    Disappearance,
    Prognosis,
    IncomingControl,
    Vocation,
    Vnosok,
    TransferInState,
    Permission,
    AdoptionInState,
    Assignment,
)


class DismissalCreateForm(forms.ModelForm):

    class Meta:
        model = Dismissal
        fields = (
            'dismissal_date',
            'order_date',
            'order_number',
            'dismissal_basis',
            'dismissal_reason',
        )


class AssignmentCreateForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = (
            'order_number',
            'order_date',
            'start_on',
            'expire',
            'factory',
            'city',
            'polish_border',
            'ukrainian_border',
            'dismissal_reason',
            'reason_number',
            'reason_date',
            'dismissal_basis',
            'basis_number',
            'basis_date',
        )


class AdoptionCreateForm(forms.ModelForm):

    class Meta:
        model = AdoptionInState
        fields = (
            'employer',
            'dismissal_date',
            'order_date',
            'order_number',
            'position',
        )


class TransferCreateForm(forms.ModelForm):

    class Meta:
        model = TransferInState
        fields = (
            'dismissal_date',
            'order_date',
            'order_number',
        )


class PermissionCreateForm(forms.ModelForm):

    class Meta:
        model = Permission
        fields = (
            'prediction_date',
            'input_date',
            'receiving_date',
            'voivodship',
            'factory',
            'employer',
            'start_date',
            'expire',
            'note',
            'scan_copy',
        )


class VnosokCreateForm(forms.ModelForm):

    class Meta:
        model = Vnosok
        fields = (
            'employer',
            'factory',
            'position',
            'start_on',
            'expire',
        )


class VocationCreateForm(forms.ModelForm):

    class Meta:
        model = Vocation
        fields = (
            'type',
            'period',
            'start_on',
            'expire',
            'order_date',
            'order_number',
            'comment',
        )


class ControlCreateForm(forms.ModelForm):

    class Meta:
        model = IncomingControl
        fields = (
            'expire',
            'factory',
        )


class PrognosisCreateForm(forms.ModelForm):
    # agree = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = Prognosis
        fields = (
            'agree',
            'expire',
            'reason',
        )


class DisappearanceCreateForm(forms.ModelForm):

    class Meta:
        model = Disappearance
        fields = (
            'violation_date',
            'appeal_date',
        )
