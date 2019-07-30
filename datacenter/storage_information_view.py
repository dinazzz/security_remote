from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits_info = []
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    
    for visit in non_closed_visits:
        info = {
            "who_entered": visit.passcard.owner_name,
            "entered_at": visit.entered_at,
            "duration": format_duration(visit.get_duration())
            }
        non_closed_visits_info.append(info)
    
    context = {
        "non_closed_visits": non_closed_visits_info,
    }
    return render(request, 'storage_information.html', context)
