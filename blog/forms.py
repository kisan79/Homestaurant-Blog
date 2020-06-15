#Blog Post Form
from django import forms
from .models import Post

#Post Form
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control-lg','placeholder':'Enter title'}),
            'slug':forms.TextInput(attrs={'class':'form-control-lg','placeholder':'Enter SEO Friendly Text'}),
            'author':forms.Select(attrs={'class':'form-control-lg',}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Write Your Content...'}),
            'publish':forms.DateTimeInput(attrs={'class':'form-control-lg',}),
            'status':forms.Select(attrs={'class':'form-control-lg',}),
            'pic1':forms.FileInput(attrs={'class':'form-control-file',})
        }