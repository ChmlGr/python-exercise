from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import SevenPairsForm
from . import utils

RESULT = 50


def seven_pairs(request):
    if request.method == 'POST':
        form = SevenPairsForm(request.POST)
        if form.is_valid():
            values = form.cleaned_data['values']
            pairs = utils.find_pairs(values, 7)
            messages.add_message(request, RESULT, pairs)

            return HttpResponseRedirect(reverse('seven_pairs'))
    else:
        form = SevenPairsForm()

    return render(request, 'seven/seven.html', {'form': form})
