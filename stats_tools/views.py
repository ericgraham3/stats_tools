import csv

from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from django.template.context_processors import request

from .forms import RandomSampleForm, UploadCsvForm
from random_sample import RandomSample


def index(request):
    """Landing page for stats tools"""
    return render(request, 'stats_tools/index.html')


def random_sample(request):
    if request.method == 'POST':
        form = RandomSampleForm(request.POST)
        if form.is_valid():
            # retrieve input values from form
            min_value = form.cleaned_data['min_value']
            max_value = form.cleaned_data['max_value']
            rows = form.cleaned_data['rows']
            columns = form.cleaned_data['columns']
            export_csv = form.cleaned_data['export']

            # Create RandomSample object
            random_sample_instance = RandomSample(min_value, max_value)

            # Call the method to get results
            results = random_sample_instance.random_table(rows, columns, export_csv)

            if export_csv:
                # Return the CSV as a response
                response = HttpResponse(results, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename=table.csv"'
                return response
            else:
                # Pass the results to the template
                return render(request, 'stats_tools/random_sample_results.html', {'results': results})

    else:
        # Display the form for GET requests
        form = RandomSampleForm()

    return render(request, 'stats_tools/random_sample.html', {'form': form})


def upload_csv(request):
    if request.method == 'POST':
        form = UploadCsvForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.files['csv_file']
            dataframe = pd.read_csv(csv_file)
    else:
        form = UploadCsvForm()

    return render(request, 'stats_tools/upload_csv.html', {'form': form})