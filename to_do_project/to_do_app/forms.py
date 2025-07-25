from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Task, Tags


User = get_user_model()

class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'task'}),
        required=False,
    )

    class Meta:
        model = Task
        fields = ['task_name', 'description', 'due_date', 'tags']
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'task', 'placeholder': 'Task name'}),
            'description': forms.Textarea(attrs={'class': 'task', 'placeholder': 'Description'}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'task', 'placeholder': 'Deadline'}),
        }



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'reg', 'placeholder': 'Email field'}))
    first_name = forms.CharField(max_length=45, required=True, widget=forms.TextInput(attrs={'class': 'reg', 'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=45, required=True, widget=forms.TextInput(attrs={'class': 'reg', 'placeholder': 'Last name'}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'class': 'reg', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'class': 'reg', 'placeholder': 'Repeat Password'}))
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email','password1' , 'password2']

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

        widgets = {
            'email' : forms.EmailInput(attrs={'class': 'reset_pass'})
        }


class TaskSearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=False, label="Пошук за назвою", widget=forms.TextInput(attrs={'class': 'searching', 'placeholder':'search'}))



class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-login', 'placeholder': 'Enter email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-login', 'placeholder': 'Enter password'}))
