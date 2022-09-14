from django import forms
from .models import Todo


class TodoCreatForm(forms.Form):
    titel=forms.CharField(required=False)
    body=forms.CharField()
    created=forms.DateTimeField()


class TodoupdateForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=('name','body','crated')
        # fields ='__all__'   hame item ha


