from django import forms 
from .models import Project 
 
class ProjectForm(forms.ModelForm): 
    class Meta: 
        model = Project 
        fields = ['topic', 'languages_used', 'duration'] 
        widgets = { 
            'topic': forms.TextInput(attrs={'placeholder': 'Enter project topic'}), 
            'languages_used': forms.Textarea(attrs={'placeholder': 'Enter languages used'}), 
            'duration': forms.NumberInput(attrs={'placeholder': 'Enter duration in weeks'}), 
        } 
        labels = { 
            'topic': 'Project Topic',  # Custom label for "topic" 
            'languages_used': 'Languages Used for the Project',  # Custom label for 
"languages_used" 
            'duration': 'Duration (Weeks)',  # Custom label for "duration"
        }