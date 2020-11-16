from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('yazan','emmail','yorum','post')

        widgets = {
            'yazan': forms.TextInput(attrs={'class':'form-control','placeholder':'Adınız'}),
            'emmail': forms.EmailInput(attrs={'class':'form-control','placeholder':'E-Mail Adresiniz'}),
            'yorum': forms.Textarea(attrs={'rows':4 , 'cols':75 , 'class': 'form-control','placeholder':'Yorumunuz'}),
        }
