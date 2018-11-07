from django import forms

from user_profile.models import User
from .models import UkrainianPassport, ForeignPassport, Visa, PersonalID


class UAPassportCreateForm(forms.ModelForm):

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


class ForeignPassportCreateForm(forms.ModelForm):

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


class UAPassportUpdateForm(forms.ModelForm):

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

    def __init__(self, pk, *args, **kwargs):
        super(UAPassportUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        passport = user.pasports.get(id=1)
        self.fields['series'].initial = passport.series
        self.fields['number'].initial = passport.number
        self.fields['place_of_issue'].initial = passport.place_of_issue
        self.fields['date_of_issue'].initial = passport.date_of_issue
        self.fields['first_page'].initial = passport.first_page
        self.fields['second_page'].initial = passport.second_page
        self.fields['registration'].initial = passport.registration


class ForeignPassportUpdateForm(forms.ModelForm):

    class Meta:
        model = ForeignPassport
        fields = (
            'number',
            'authority',
            'date_of_expiry',
            'first_page',
        )

    def __init__(self, pk, *args, **kwargs):
        super(ForeignPassportUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        passport = user.foreign_pasport.get(id=1)
        self.fields['number'].initial = passport.number
        self.fields['authority'].initial = passport.authority
        self.fields['date_of_expiry'].initial = passport.date_of_expiry
        self.fields['first_page'].initial = passport.first_page


class VisaUpdateForm(forms.ModelForm):

    class Meta:
        model = Visa
        fields = (
            'first_date',
            'prediction_date',
            'start_on',
            'expire',
            'visa_scan',
        )

    def __init__(self, pk, *args, **kwargs):
        super(VisaUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        visa = user.visas.get(id=1)
        self.fields['first_date'].initial = visa.first_date
        self.fields['prediction_date'].initial = visa.prediction_date
        self.fields['start_on'].initial = visa.start_on
        self.fields['expire'].initial = visa.expire
        self.fields['visa_scan'].initial = visa.visa_scan


class PersonalIDUpdateForm(forms.ModelForm):

    class Meta:
        model = PersonalID
        fields = (
            'personal_id',
            'scan_id',
        )

    def __init__(self, pk, *args, **kwargs):
        super(PersonalIDUpdateForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        personal_id = user.personal_id.get(id=1)
        self.fields['personal_id'].initial = personal_id.personal_id
        self.fields['scan_id'].initial = personal_id.scan_id
