from django import forms
from . models import Article

class addBlog(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author','title','text']
        widgets={'author':forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Author'
        }),
        'title':forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Title'

        }),
        'text':forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Add your Blog here',
        'rows':'10',
        }),
        }

class editBlog(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','text']
        widgets={
        'title':forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Title'

        }),
        'text':forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Add your Blog here',
        'rows':'10',
        }),
        }
