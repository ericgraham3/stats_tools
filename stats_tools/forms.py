from django import forms

from .models import RandomSample


class RandomSampleForm(forms.ModelForm):
    class Meta:
        model = RandomSample
        fields = ['min_value', 'max_value', 'rows', 'columns', 'export']
        labels = {'min_value': 'Minimum Value',
                  'max_value': 'Maximum Value',
                  'rows': 'Number of results to return:',
                  'columns': 'Number of columns to return',
                  'export': 'Export as CSV?'}

    def __init__(self, *args, **kwargs):
        super(RandomSampleForm, self).__init__(*args, **kwargs)

        # Set the default value for 'columns' field to 1
        self.fields['columns'].initial = 1

class UploadCsvForm(forms.Form):
    csv_file = forms.FileField()
