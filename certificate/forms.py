from django import forms
from .models import (
    Interview,
    Certificate,
    Test,
    Training,
    Polish,
)


class InterviewCreateForm(forms.ModelForm):

    class Meta:
        model = Interview
        fields = (
            'start_on',
            'type',
            'result',
        )


class CertificateCreateForm(forms.ModelForm):

    class Meta:
        model = Certificate
        fields = (
            'certification_date',
            'paying_date',
            'welding_type',
            'start_on',
            'expire',
            'certificate_scan',
        )


class TestCreateForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = (
            'start_on',
            'type',
            'result',
        )


class TrainingCreateForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = (
            'start_on',
            'expire',
            'result',
        )


class PolishCreateForm(forms.ModelForm):

    class Meta:
        model = Polish
        fields = (
            'solo',
            'course',
        )
