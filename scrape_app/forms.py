from django import forms

class SearchProductForm(forms.Form):
    teachers = forms.CharField(required=True, max_length=50)
