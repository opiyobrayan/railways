from django.contrib import admin
from . models import ActivityDetail, AddParticipant,Organization,Participant,PersonContact,Grant,AddParticipant
# Register your models here.

class ParticipantInlineAdmin(admin.TabularInline):
    model=Participant

class Activity_DetailAdmin(admin.ModelAdmin):
    inlines=[ParticipantInlineAdmin]

admin.site.register(AddParticipant,Activity_DetailAdmin)
admin.site.register(PersonContact)
admin.site.register(Organization)
admin.site.register(Grant)
admin.site.register(ActivityDetail)


# admin.site.register(Participant)