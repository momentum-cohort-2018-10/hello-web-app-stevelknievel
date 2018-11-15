from django.shortcuts import render
from collection.forms import VoiceOverEquipmentForm
from collection.models import VoiceOverEquipment


# Create your views here.
def index(request):
    # defining the variable
    voiceoverequipments = VoiceOverEquipment.objects.all()
    # this is your new view.
    return render(request, 'index.html', {
        'voiceoverequipments': voiceoverequipments,
    })


def voiceoverequipment_detail(request, slug):
    # grab the object...
    voiceoverequipment = VoiceOverEquipment.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'voiceoverequipments/voiceoverequipment_detail.html', {
        'voiceoverequipment': voiceoverequipment,
    })


def edit_voiceoverequipment(request, slug):
    # grab the object...
    voiceoverequipment = VoiceOverEquipment.objects.get(slug=slug)
    # set the form we're using...
    form_class = VoiceOverEquipmentForm
    # if we're coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=voiceoverequipment)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('voiceoverequipment_detail', slug=voiceoverequipment.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=voiceoverequipment)

    # and render the template
    return render(request, 'voiceoverequipments/edit_voiceoverequipment.html', {
        'voiceoverequipment': voiceoverequipment,
        'form': form,
    })