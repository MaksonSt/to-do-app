from django import forms
from .models import ListOfTasks



class ListTasksForm(forms.ModelForm):
    class Meta:
        model = ListOfTasks
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'task-list', 'placeholder': 'Enter name of list of task'})
        }