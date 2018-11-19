from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
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


@login_required
def edit_voiceoverequipment(request, slug):
    # grab the object...
    voiceoverequipment = VoiceOverEquipment.objects.get(slug=slug)
    # make sure the logged in user isthe owner of the thing
    if voiceoverequipment.user != request.user:
        raise Http404
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


def create_voiceoverequipment(request):
    form_class = VoiceOverEquipmentForm
    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but do not save yet
            voiceoverequipment = form.save(commit=False)
            # set the additional details
            voiceoverequipment.user = request.user
            voiceoverequipment.slug = slugify(voiceoverequipment.name)
            # save the object
            voiceoverequipment.save()
            # redirect to our newly created thing
            return redirect('voiceoverequipment_detail', slug=voiceoverequipment.slug)
    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'voiceoverequipments/create_voiceoverequipment.html', {
        'form': form,
    })


def browse_by_name(request, initial=None):
    if initial:
        voiceoverequipments = Voiceoverequipment.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        voiceoverequipments = Voiceoverequipment.objects.all().order_by('name')
    return render(request, 'search/search.html', {
        'voiceoverequipments': voiceoverequipments,
        'initial': initial,
    })