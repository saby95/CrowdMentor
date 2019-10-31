from django import forms
from .models import UserRoles
from django.contrib.auth.models import User
from profile import Profile

class ChangeRolesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.users = kwargs.pop('users')  # user was passed to a single form
        super(ChangeRolesForm, self).__init__(*args, **kwargs)

        for key, value in self.users.items():
            label= ''
            choices = [(tag.value, tag.value) for tag in UserRoles]
            choices.insert(0, ('Select', 'Select'));
            self.fields['role_'+str(key)] = forms.ChoiceField(choices=choices, initial=value[3],label=label, required=False)
            self.fields['salary_'+str(key)] = forms.FloatField(label='Salary', initial=value[3], required=False)
            self.fields['bonus_' + str(key)] = forms.FloatField(label='Bonus', initial=value[4], required=False)
            self.fields['fine_' + str(key)] = forms.FloatField(label='Fine', initial=value[5], required=False)
            self.fields['audit_prob_' + str(key)] = forms.FloatField(label='Audit Probability', initial=value[6], required=False)
            # self.fields['role_' + str(key)].initial = value[2]


