from django import forms
from django.forms import ModelForm
from .models import Skill, Language, Work, Education, Objective, About



class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['sk','percent']

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['lg','percent']

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['description']

class DateInput(forms.DateInput):
    input_type = 'date'

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['company','position','location', 'work_description', 'start_date', 'end_date']
        widgets= { 'start_date': DateInput(), 'end_date': DateInput()}


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution_name','degree', 'location', 'graduation_year', 'description']
        widgets= { 'graduation_year': DateInput()}


class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = ['description']
