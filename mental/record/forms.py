from django import forms

from .models import Record


class AddRecordForm(forms.ModelForm):
    record_date = forms.DateField(required=True,
                                 widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    record = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Record
        fields = ['record_date', 'record']