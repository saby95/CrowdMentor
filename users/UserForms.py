from django import forms
from .models import UserRoles, TRUE_OR_FALSE, pool_choices
from django.contrib.auth.models import User
from django.forms.forms import NON_FIELD_ERRORS

class ChangeRolesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        value = kwargs.pop('value')
        usr = User.objects.get(id=value)
        super(ChangeRolesForm, self).__init__(*args, **kwargs)

        choices = []
        for tag in UserRoles:
            if tag.value is not 'admin':
                choices.append((tag.value,tag.value))
        # choices = [(tag.value, tag.value) for tag in UserRoles]
        # worker alone -> mentor, TU, AU
        # mentor + worker -> worker
        # TU -> AU
        # AU -> TU
        # TU + AU -> TU, AU
        # self.show_compensation = (UserRoles.WORKER.value or UserRoles.AUDITOR.value) in  usr.profile.get_roles()
        profile_roles = ""
        for element in usr.profile.get_roles():
            profile_roles += str(element)+","
        profile_roles = profile_roles[:-1]    

        current_roles = usr.profile.get_roles()

        self.fields['existing_role'] = forms.CharField(initial=profile_roles, widget=forms.TextInput(attrs={'readonly':'readonly','class':'input'}))
        if(len(current_roles) == 1 and current_roles[0] == 'worker'):
            choices = [('mentor','mentor'),('task_updater','task_updater'),('auditor','auditor')]
        elif(len(current_roles) == 2 and 'mentor' in current_roles):
            choices = [('worker','worker')]
        elif(len(current_roles) == 1 and current_roles[0] == 'task_updater'):
            choices = [('auditor','auditor')]
        elif(len(current_roles) == 1 and current_roles[0] == 'auditor'):
            choices = [('task_updater','task_updater')]
        else:
            choices = [('task_updater','task_updater'),('auditor','auditor')]

        choices.insert(0,('Select','Select'))

        self.fields['role'] = forms.ChoiceField(choices=choices, required=False)      
        self.fields['salary'] = forms.FloatField(label='Salary', initial=usr.profile.salary, required=True, widget=forms.TextInput(attrs={'class':'input'}))
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
