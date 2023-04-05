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

            record = record_add_form.cleaned_data.get('record')
            record.submitter = request.user

            # submitter_profile = Profile.objects.get(id=request.user.id)

            # submitter_profile.save()

            record.save()

            messages.success(request, 'Your event is added successfully')
            return redirect(to='event_list')
    else:
        record_add_form = AddRecordForm(instance=request.user)
    return render(request, 'record/add_record.html', {'form': record_add_form})


def record_list(request):
    record_list = Record.objects.all()

    return render(request, 'record/list_record.html', {'record_list': record_list})
