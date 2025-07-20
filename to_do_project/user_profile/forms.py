from django import forms
from django.contrib.auth import get_user_model
from .models import UserProfile



User = get_user_model()

class NameChangeForm(forms.ModelForm):
    new_name = forms.CharField(max_length=45, required=True, widget=forms.TextInput(attrs={'class': 'input-name-change', 'placeholder': 'Enter new name'}))

    class Meta:
        model = User
        fields = []

    def clean_new_name(self):
        new_name = self.cleaned_data.get('new_name')
        if new_name and User.objects.filter(name=new_name).exists():
            raise forms.ValidationError("This name already exists")
        return new_name




class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'date_of_birth', 'background_color']

        widgets = {
            'bio': forms.TextInput(attrs={'class': 'input-update-profile', 'placeholder': 'Describe yourself', 'rows': 4}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'input-update-profile', 'placeholder': 'Image'}),
            'date_of_birth': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'input-update-profile', 'placeholder': 'Date of birth'}),
            'background_color': forms.TextInput(attrs={'type': 'color', 'class': 'input-update-profile'})
        }