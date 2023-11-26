from django import forms
from .models import *
from django.forms import ModelForm

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('first_name','last_name','address','phone','email','facebook_link','git_link','linkedin_link','twitter_link','career_obj','profile_img')

        labels = {
            'first_name':'',
            'last_name':'',
            'address':'',
            'phone':'',
            'email':'',
            'facebook_link':'',
            'git_link':'',
            'linkedin_link':'',
            'twitter_link':'',
            'career_obj':'',

        }

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'facebook_link':forms.TextInput(attrs={'class':'form-control','placeholder':'Facebook Link'}),
            'git_link':forms.TextInput(attrs={'class':'form-control','placeholder':'GitHub Link'}),
            'linkedin_link':forms.TextInput(attrs={'class':'form-control','placeholder':'Linkedin Link'}),
            'twitter_link':forms.TextInput(attrs={'class':'form-control','placeholder':'Twitter Link'}),
            'career_obj':forms.Textarea(attrs={'class':'form-control','placeholder':'Career Objective'}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('institute_name','degree','department','result','passed_year')

        labels = {
            'institute_name':'',
            'degree':'',
            'department':'',
            'result':'',
            'passed_year':'',

        }

        widgets = {
            'institute_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name Of The Institute'}),
            'degree': forms.TextInput(attrs={'class':'form-control','placeholder':'Degree'}),
            'department': forms.TextInput(attrs={'class':'form-control','placeholder':'Department'}),
            'result':forms.TextInput(attrs={'class':'form-control','placeholder':'Result'}),
            'passed_year':forms.DateInput(attrs={'class':'form-control','placeholder':'Result','type':'date'})
        }

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ('description',)

        labels = {
            'description':''
        }

        widgets = {
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Interest Description',}),
        }

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference 
        fields = ('name','post','work_on','email')

        labels = {
            'name':'',
            'post':'',
            'work_on':'',
            'email':'',

        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'post':forms.TextInput(attrs={'class':'form-control','placeholder':'Post Name'}),
            'work_on':forms.TextInput(attrs={'class':'form-control','placeholder':'Department Name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','github_link')

        labels={
            'title':'',
            'github_link':'',
        }

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Project Title'}),
            'github_link':forms.TextInput(attrs={'class':'form-control','placeholder':'Git-Hub Link'}),
        }