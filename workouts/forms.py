from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Please select a date (YYYY-MM-DD)"
    )

    class Meta:
        model = Workout
        fields = ['date', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
        }