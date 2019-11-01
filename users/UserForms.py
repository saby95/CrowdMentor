from django import forms
from .models import UserRoles, TRUE_OR_FALSE
from django.contrib.auth.models import User
from profile import Profile

class ChangeRolesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        #self.users = kwargs.pop('users')  # user was passed to a single form
        value = kwargs.pop('value')
        usr = User.objects.get(id=value)
        super(ChangeRolesForm, self).__init__(*args, **kwargs)

        choices = [(tag.value, tag.value) for tag in UserRoles]
        self.is_worker = (usr.profile.role==UserRoles.NORMAL_WORKER.value)
        self.fields['existing_role'] = forms.CharField(initial=usr.profile.role,
                                                       widget=forms.TextInput(attrs={'readonly':'readonly'}))
        self.fields['role'] = forms.ChoiceField(choices=choices, initial=usr.profile.role, required=False)
        self.fields['salary'] = forms.FloatField(label='Salary', initial=usr.worker.salary, required=False)
        self.fields['bonus'] = forms.FloatField(label='Bonus', initial=usr.worker.bonus, required=False)
        self.fields['fine'] = forms.FloatField(label='Fine', initial=usr.worker.fine, required=False)
        self.fields['audit_prob'] = forms.FloatField(label='Audit Probability', initial=usr.worker.audit_prob_user, required=False)

        # for key, value in self.users.items():
        #     label= ''
        #     choices = [(tag.value, tag.value) for tag in UserRoles]
        #     choices.insert(0, ('Select', 'Select'));
        #     self.fields['role_'+str(key)] = forms.ChoiceField(choices=choices, initial=value[3],label=label, required=False)
        #     self.fields['salary_'+str(key)] = forms.FloatField(label='Salary', initial=value[4], required=False)
        #     self.fields['bonus_' + str(key)] = forms.FloatField(label='Bonus', initial=value[5], required=False)
        #     self.fields['fine_' + str(key)] = forms.FloatField(label='Fine', initial=value[6], required=False)
        #     self.fields['audit_prob_' + str(key)] = forms.FloatField(label='Audit Probability', initial=value[7], required=False)
            # self.fields['role_' + str(key)].initial = value[2]


class ChangeMentorStatus(forms.Form):
    def __init__(self, *args, **kwargs):
        value = kwargs.pop('value')
        super(ChangeMentorStatus, self).__init__(*args, **kwargs)

        self.fields["mentor_status"] = forms.ChoiceField(choices=TRUE_OR_FALSE, initial=value)
