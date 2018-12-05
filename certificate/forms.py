from django import forms

from user_profile.models import User
from .models import (
    Interview,
    Certificate,
    Test,
    Training,
    Polish,
    QualificationLevel, PostQualificationLevel)


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


class LocksmithCreateForm(forms.ModelForm):

    class Meta:
        model = QualificationLevel
        fields = (
            'draw_reading',
            'candle',
            'bulgarian',
            'semiautomatic',
        )


class WelderCreateForm(forms.ModelForm):

    class Meta:
        model = QualificationLevel
        fields = (
            'welding_method',
            'metal_brand',
            'connection_type',
            'spatial_posture',
            'thickness',
        )


class OtherCreateForm(forms.ModelForm):

    class Meta:
        model = QualificationLevel
        fields = (
            'other',
        )


class PostLocksmithCreateForm(forms.ModelForm):

    class Meta:
        model = PostQualificationLevel
        fields = (
            'draw_reading',
            'candle',
            'bulgarian',
            'semiautomatic',
        )


class PostWelderCreateForm(forms.ModelForm):

    class Meta:
        model = PostQualificationLevel
        fields = (
            'welding_method',
            'metal_brand',
            'connection_type',
            'spatial_posture',
            'thickness',
        )


class PostOtherCreateForm(forms.ModelForm):

    class Meta:
        model = PostQualificationLevel
        fields = (
            'other',
        )


class InterviewUpdateForm(forms.ModelForm):

    class Meta:
        model = Interview
        fields = (
            'start_on',
            'type',
            'result',
        )

    # def __init__(self, pk, *args, **kwargs):
    #     super(InterviewUpdateForm, self).__init__(*args, **kwargs)
    #     user = User.objects.get(pk=pk)
    #     interview = user.interviews.get(id=1)
    #     self.fields['start_on'].initial = interview.start_on
    #     self.fields['type'].initial = interview.type
    #     self.fields['result'].initial = interview.result


class CertificateUpdateForm(forms.ModelForm):

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

    # def __init__(self, pk, *args, **kwargs):
    #     super(CertificateUpdateForm, self).__init__(*args, **kwargs)
    #     user = User.objects.get(pk=pk)
    #     certificates = user.certificates.get(id=1)
    #     self.fields['certification_date'].initial = certificates.certification_date
    #     self.fields['paying_date'].initial = certificates.paying_date
    #     self.fields['welding_type'].initial = certificates.welding_type
    #     self.fields['start_on'].initial = certificates.start_on
    #     self.fields['expire'].initial = certificates.expire
    #     self.fields['certificate_scan'].initial = certificates.certificate_scan


class TestUpdateForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = (
            'start_on',
            'type',
            'result',
        )

    # def __init__(self, pk, *args, **kwargs):
    #     super(TestUpdateForm, self).__init__(*args, **kwargs)
    #     user = User.objects.get(pk=pk)
    #     test = user.tests.get(id=1)
    #     self.fields['start_on'].initial = test.start_on
    #     self.fields['type'].initial = test.type
    #     self.fields['result'].initial = test.result


class TrainingUpdateForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = (
            'start_on',
            'expire',
            'result',
        )

    # def __init__(self, pk, *args, **kwargs):
    #     super(TrainingUpdateForm, self).__init__(*args, **kwargs)
    #     user = User.objects.get(pk=pk)
    #     training = user.trainings.get(id=1)
    #     self.fields['start_on'].initial = training.start_on
    #     self.fields['expire'].initial = training.expire
    #     self.fields['result'].initial = training.result


class PolishUpdateForm(forms.ModelForm):

    class Meta:
        model = Polish
        fields = (
            'solo',
            'course',
        )

    # def __init__(self, pk, *args, **kwargs):
    #     super(PolishUpdateForm, self).__init__(*args, **kwargs)
    #     user = User.objects.get(pk=pk)
    #     polish = user.polish.get(id=1)
    #     self.fields['start_on'].initial = polish.solo
    #     self.fields['type'].initial = polish.course


class LocksmithUpdateForm(forms.ModelForm):

    class Meta:
        model = QualificationLevel
        fields = (
            'draw_reading',
            'candle',
            'bulgarian',
            'semiautomatic',
        )


class WelderUpdateForm(forms.ModelForm):

    class Meta:
        model = QualificationLevel
        fields = (
            'welding_method',
            'metal_brand',
            'connection_type',
            'spatial_posture',
            'thickness',
        )


class OtherUpdateForm(forms.ModelForm):

    class Meta:
        model = QualificationLevel
        fields = (
            'other',
        )


class PostLocksmithUpdateForm(forms.ModelForm):

    class Meta:
        model = PostQualificationLevel
        fields = (
            'draw_reading',
            'candle',
            'bulgarian',
            'semiautomatic',
        )


class PostWelderUpdateForm(forms.ModelForm):

    class Meta:
        model = PostQualificationLevel
        fields = (
            'welding_method',
            'metal_brand',
            'connection_type',
            'spatial_posture',
            'thickness',
        )


class PostOtherUpdateForm(forms.ModelForm):

    class Meta:
        model = PostQualificationLevel
        fields = (
            'other',
        )
