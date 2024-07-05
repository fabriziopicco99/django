from django import forms
from .models import Avatar

class AvatarForm(forms.ModelForm):
    
    # name = forms.CharField(label='Nombre', required=False)
    # last_name = forms.CharField(label='Apellido', required=False)
    # email = forms.EmailField(label='Email', required=False)
    # image = forms.ImageField(label='Avatar', required=False)
    
    class Meta:
        model = Avatar
        fields = ['name','last_name', 'email', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }