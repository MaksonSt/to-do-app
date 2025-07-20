from django import forms
from django.contrib.auth import get_user_model



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
