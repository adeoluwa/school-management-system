from dataclasses import fields
from tkinter import Widget
from django import forms

from stud_app.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'field_of_study']
        labels={
            'student_number':'student_number',
            'first_name':'first_name',
            'last_name':'last_name',
            'field_of_study':'field_of_study'
        }
        widgets = {
            'student_number': forms.NumberInput(attrs ={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'field_of_study':forms.TextInput(attrs={'class':'form-control'}),
        }