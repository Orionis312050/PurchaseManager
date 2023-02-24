from django import forms
from .models import Depense

class DepForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = "__all__"