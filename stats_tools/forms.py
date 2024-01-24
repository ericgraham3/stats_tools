from django import forms

from .models import RandomSample


class RandomSampleForm(forms.ModelForm):
    class Meta:
        model = RandomSample
        fields = ['min_value', 'max_value', 'rows']
        labels = {'min_value': 'Minimum Value', 'max_value': 'Maximum Value', 'rows': 'Number of results to return:'}
