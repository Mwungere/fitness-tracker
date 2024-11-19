# forms.py

from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'duration', 'date', 'activity_type']
        widgets = { 
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Activity Name'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Duration (e.g., 2:00:00)'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'activity_type': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['duration'].widget.attrs.update({'class': 'form-control'})
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['activity_type'].widget.attrs.update({'class': 'form-select'})
