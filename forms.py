from django import forms
from .models import question_form


class question_data(forms.ModelForm):
    class Meta:
        model = question_form
        fields = ('questions','opt1','opt2','opt3','opt4')
