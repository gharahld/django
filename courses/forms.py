from django import forms
from .models import Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'tittle'
        ]
    def clean_title(self):
        tittle = self.cleaned_data.get('tittle')
        if tittle.lower() == 'abc:':
            raise forms.ValidationError('This is not a valid tittle')
        return tittle
