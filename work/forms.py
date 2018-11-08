from django import forms

from user_profile.models import User
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


class DismissalUpdateForm(forms.ModelForm):

    class Meta:
        model = Dismissal
        fields = (
            'dismissal_date',
            'order_date',
            'order_number',
            'dismissal_basis',
            'dismissal_reason',
        )

    def __init__(self, pk, *args, **kwargs):
        super(DismissalUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        dismissal = user.dismissals.get(id=1)
        self.fields['type'].initial = dismissal.type
        self.fields['contact'].initial = dismissal.contact


class AssignmentUpdateForm(forms.ModelForm):

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

    def __init__(self, pk, *args, **kwargs):
        super(AssignmentUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        assignment = user.assignments.get(id=1)
        self.fields['type'].initial = assignment.type
        self.fields['contact'].initial = assignment.contact


class AdoptionUpdateForm(forms.ModelForm):

    class Meta:
        model = AdoptionInState
        fields = (
            'employer',
            'dismissal_date',
            'order_date',
            'order_number',
            'position',
        )

    def __init__(self, pk, *args, **kwargs):
        super(AdoptionUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        adoption = user.adoptions.get(id=1)
        self.fields['type'].initial = adoption.type
        self.fields['contact'].initial = adoption.contact


class TransferUpdateForm(forms.ModelForm):

    class Meta:
        model = TransferInState
        fields = (
            'dismissal_date',
            'order_date',
            'order_number',
        )

    def __init__(self, pk, *args, **kwargs):
        super(TransferUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        transfer = user.transfers.get(id=1)
        self.fields['type'].initial = transfer.type
        self.fields['contact'].initial = transfer.contact


class PermissionUpdateForm(forms.ModelForm):

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

    def __init__(self, pk, *args, **kwargs):
        super(PermissionUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        permission = user.permissions.get(id=1)
        self.fields['type'].initial = permission.type
        self.fields['contact'].initial = permission.contact


class VnosokUpdateForm(forms.ModelForm):

    class Meta:
        model = Vnosok
        fields = (
            'employer',
            'factory',
            'position',
            'start_on',
            'expire',
        )

    def __init__(self, pk, *args, **kwargs):
        super(VnosokUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        vnosok = user.vnosok_list.get(id=1)
        self.fields['type'].initial = vnosok.type
        self.fields['contact'].initial = vnosok.contact


class VocationUpdateForm(forms.ModelForm):

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

    def __init__(self, pk, *args, **kwargs):
        super(VocationUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        vocation = user.vocations.get(id=1)
        self.fields['type'].initial = vocation.type
        self.fields['contact'].initial = vocation.contact


class ControlUpdateForm(forms.ModelForm):

    class Meta:
        model = IncomingControl
        fields = (
            'expire',
            'factory',
        )

    def __init__(self, pk, *args, **kwargs):
        super(ControlUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        control = user.incoming_controls.get(id=1)
        self.fields['type'].initial = control.type
        self.fields['contact'].initial = control.contact


class PrognosisUpdateForm(forms.ModelForm):
    # agree = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = Prognosis
        fields = (
            'agree',
            'expire',
            'reason',
        )

    def __init__(self, pk, *args, **kwargs):
        super(PrognosisUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        prognosis = user.prognoses.get(id=1)
        self.fields['type'].initial = prognosis.type
        self.fields['contact'].initial = prognosis.contact


class DisappearanceUpdateForm(forms.ModelForm):

    class Meta:
        model = Disappearance
        fields = (
            'violation_date',
            'appeal_date',
        )

    def __init__(self, pk, *args, **kwargs):
        super(DisappearanceUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        disappearance = user.disappearances.get(id=1)
        self.fields['type'].initial = disappearance.type
        self.fields['contact'].initial = disappearance.contact
