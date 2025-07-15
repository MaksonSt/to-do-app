from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'due_date']

        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=45, required=True)
    class Meta:
        model = User
        fields = ['name', 'email','password1' , 'password2']

    class RegistrationForm(UserCreationForm):
        email = forms.EmailField(required=True)
        name = forms.CharField(max_length=45, required=True)

        class Meta:
            model = User
            fields = ['name', 'email', 'password1', 'password2']

        def clean(self):
            cleaned_data = super().clean()
            email = cleaned_data.get('email')
            if email and User.objects.filter(email=email).exists():
                self.add_error('email', 'Email already exist')
            return cleaned_data



class ResetPasswordForm(forms.Form):
    email = forms.EmailField()
    class Meta:
        fields = ['email']



class TaskSearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=False, label="Пошук за назвою")
