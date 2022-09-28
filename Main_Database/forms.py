from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import Participant,AddParticipant,Poll,ActivityDetail,Organization,Grant
from django.forms.models import inlineformset_factory,modelformset_factory

class ParticipantForm(ModelForm):
    class Meta:
        model=Participant
        fields='__all__'

        labels={
            'activity':'Activity',
            'name':'',
            'id_number':'',
            'phone':'',
            'organization':'Select Organization',
            'gender':' Select Gender',
            'type':' Select Participant Type',
            'county':'Select County',
             'email':'',
        }
        widgets={
            'activity':forms.Select(attrs={'class':'form-control','placeholder':'Thematic Area'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'id_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Id Number'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'organization':forms.Select(attrs={'class':'form-control','placeholder':'Organization'}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':'Gender'}),
            'type':forms.Select(attrs={'class':'form-control','placeholder':'Type'}),
            'county':forms.TextInput(attrs={'class':'form-control','placeholder':'County'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})

        }

class CreatePollForm(forms.ModelForm):

    class Meta:
        model=Poll
        fields=['thematic','activity','question','option_one','option_two','option_three','option_four','option_five','option_six']

class CreateActivityForm(forms.ModelForm):
    class Meta:
        model=ActivityDetail
        fields="__all__"

class CreateOrganizationForm(forms.ModelForm):
    class Meta:
        model=Organization
        fields="__all__"
class CreateProjectForm(forms.ModelForm):
    class Meta:
        model=Grant
        fields="__all__"

