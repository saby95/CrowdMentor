from django import forms
from .models import UserRoles, TRUE_OR_FALSE, pool_choices
from django.contrib.auth.models import User
from django.forms.forms import NON_FIELD_ERRORS

class ChangeRolesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        value = kwargs.pop('value')
        usr = User.objects.get(id=value)
        super(ChangeRolesForm, self).__init__(*args, **kwargs)

        choices = [(tag.value, tag.value) for tag in UserRoles]
        self.is_worker = (usr.profile.role == UserRoles.WORKER.value) or (usr.profile.role == UserRoles.AUDITOR.value)
        self.fields['existing_role'] = forms.CharField(initial=usr.profile.role, 
                                                       widget=forms.TextInput(attrs={'readonly':'readonly','class':'input'}))
        self.fields['role'] = forms.ChoiceField(choices=choices, initial=usr.profile.role, required=False)
        self.fields['salary'] = forms.FloatField(label='Salary', initial=usr.profile.salary, required=False, widget=forms.TextInput(attrs={'class':'input'}))
        self.fields['bonus'] = forms.FloatField(label='Bonus', initial=usr.profile.bonus, required=False, widget=forms.TextInput(attrs={'class':'input'}))
        self.fields['fine'] = forms.FloatField(label='Fine', initial=usr.profile.fine, required=False, widget=forms.TextInput(attrs={'class':'input'}))
        self.fields['audit_prob'] = forms.FloatField(label='Audit Probability', initial=usr.profile.audit_prob_user, required=False, widget=forms.TextInput(attrs={'class':'input'}))


class ChangeMentorStatus(forms.Form):
    def __init__(self, *args, **kwargs):
        value = kwargs.pop('value')
        super(ChangeMentorStatus, self).__init__(*args, **kwargs)

        self.fields["mentor_status"] = forms.ChoiceField(choices=TRUE_OR_FALSE, initial=value)

class AssignPools(forms.Form):
    def __init__(self, *args, **kwargs):
        value = kwargs.pop('value')
        mentors = kwargs.pop('mentors')
        
        usr = User.objects.get(id=value)
        super(AssignPools,self).__init__(*args, **kwargs)
        self.fields['radio'] = forms.ChoiceField(choices=pool_choices,initial=usr.profile.worker_pool, required=False, widget=forms.RadioSelect(attrs={'class':'radio'}))
        self.fields['mentors'] = forms.ChoiceField(choices=mentors, required=False, initial='Select')
        self.fields['mentors'].initial = 'Select'
        

class AddMentor(forms.Form):
    def __init__(self, *args, **kwargs):
        mentor_choices = kwargs.pop('mentor_choices')
        self.pool = kwargs.pop('pool')
        self.cur_mentor = kwargs.pop('cur_mentor')
        self.submitted = kwargs.pop('submitted')
        self.same_mentor = kwargs.pop('same_mentor')
        super(AddMentor, self).__init__(*args, **kwargs)

        CHOICES = [('Select','Select')]
        for choice in mentor_choices:
            CHOICES.append(choice)
        self.fields['pool'] = forms.ChoiceField(choices=pool_choices,initial=self.pool,label='Worker Pool')
        self.fields['mentor_ch'] = forms.ChoiceField(choices=CHOICES, label='Select New mentor')
        if self.pool == 'A':
            try:
                self.fields['mentor_ch'].initial = self.cur_mentor[0]
            except:
                pass
