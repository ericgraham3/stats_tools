from django.shortcuts import render

from .forms import RandomSampleForm
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

            # Create RandomSample object
            random_sample_instance = RandomSample(min_value, max_value)

            # Call the method to get results
            results = random_sample_instance.random_table(rows, 1)

            # Pass the results to the template
            return render(request, 'stats_tools/random_sample_results.html', {'results': results})

    else:
        # Display the form for GET requests
        form = RandomSampleForm()

    return render(request, 'stats_tools/random_sample.html', {'form': form})
