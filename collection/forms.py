from django.forms import ModelForm
from collection.models import VoiceOverEquipment


class VoiceOverEquipmentForm(ModelForm):
    class Meta:
        model = VoiceOverEquipment
        fields = ('name', 'description',)


# class SearchForm(forms.Form):
#     pass
