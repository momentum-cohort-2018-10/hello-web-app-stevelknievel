from django.contrib import admin


# Register your models here.
from collection.models import VoiceOverEquipment


class VoiceOverEquipmentAdmin(admin.ModelAdmin):
    model = VoiceOverEquipment
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(VoiceOverEquipment, VoiceOverEquipmentAdmin)
