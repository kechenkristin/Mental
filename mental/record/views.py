import json

from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import AddRecordForm
from .models import Record


# Create your views here.
def add_record(request):
    if request.method == 'POST':
        record_add_form = AddRecordForm(request.POST)

        if record_add_form.is_valid():
            record_add_form.save()

            record_str = record_add_form.cleaned_data.get('record')

            record = Record.objects.get(record=record_str)
            record.submitter = request.user

            # submitter_profile = Profile.objects.get(id=request.user.id)

            # submitter_profile.save()

            record.save()

            messages.success(request, 'Your record is added successfully')
            return redirect(to='record_list')
    else:
        record_add_form = AddRecordForm(instance=request.user)
    return render(request, 'record/add_record.html', {'form': record_add_form})


def record_list(request):
    record_list = Record.objects.all()

    return render(request, 'record/list_record.html', {'record_list': record_list})


def record_remove(request, eid):
    record = Record.objects.get(id=eid)

    submitter_id = record.submitter.id

    if submitter_id != request.user.id:
        messages.error(request, "You are not the submitter!")
        return redirect(to='record_list')

    Record.objects.filter(id=eid).delete()
    messages.success(request, 'You remove this record!')
    return redirect(to='record_list')


def analysis(request, rid):
    record = Record.objects.get(id=rid)
    record_str = record.record

    url = "https://advanced-emotions-detection-advemotions.p.rapidapi.com/getemotionsnon"

    querystring = {
        "text": record_str}

    headers = {
        "X-RapidAPI-Key": "5632d5510fmsh11f48e26de7c88dp1a2719jsn6c6c56277791",
        "X-RapidAPI-Host": "advanced-emotions-detection-advemotions.p.rapidapi.com"
    }

    import requests
    response = requests.request("GET", url, headers=headers, params=querystring)


    data = response.json()
    new_data_list = []

    for key, value in data.items():
        if value != 0 and key != 'success':
            new_data_list.append(key)

    context = {
        'emotions': new_data_list
    }
    return render(request, 'record/mood.html', context)