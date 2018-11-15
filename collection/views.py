from django.shortcuts import render
from collection.models import VoiceOverEquipment


# Create your views here.
def index(request):
    # defining the variable
    VoiceOverEquipments = VoiceOverEquipment.objects.all()
    # this is your new view.
    return render(request, 'index.html', {
        'VoiceOverEquipments': VoiceOverEquipments,
    })

