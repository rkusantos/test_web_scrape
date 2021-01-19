from django import forms

class SearchProductForm(forms.Form):
    product = forms.CharField(required=True, max_length=50)
