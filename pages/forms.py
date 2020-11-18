from django import forms
from .models import Contact, Support

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('title','sender','mail','text')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'sender': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.EmailInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'rows':'8' ,'cols':'10', 'class':'form-control mt-3'}),
        }

class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ('subject','title','sender','mail','text')

        widgets = {
            'subject': forms.Select(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'sender': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.EmailInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'rows':'8' ,'cols':'10', 'class':'form-control mt-3'}),
        }
