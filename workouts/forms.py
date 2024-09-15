from django import forms
from .models import Workout
from django.core.exceptions import ValidationError
from django.utils import timezone

class WorkoutForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Please enter a date (YYYY-MM-DD)",
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
    )

    class Meta:
        model = Workout
        fields = ['date', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date > timezone.now().date():
            raise ValidationError("The date cannot be in the future.")
        return date