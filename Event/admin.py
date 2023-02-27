<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 3ab9d94c055339275ba825dfc462c43b16398c1a
from django.contrib import admin, messages
from .models import *
from Person.models import Person
from datetime import datetime
# from Person.models import Person

class ParticipationsAdmin(admin.StackedInline):
    model = Event_Participation
    extra=0
# Register your models here.
@admin.register(Person)
class SearchPerson(admin.ModelAdmin):
    search_fields=['username']
class DateListFilter(admin.SimpleListFilter):
    title="Event Date"
    parameter_name = "event_date"
    def lookups(self, request, model_admin):
        return (
            ("Past Events", ("PE")),
            ("Upcoming Events", ("UE")),
            ("Today Events", ("TE")),
        )
    def queryset(self, request, queryset):
        if self.value()=="Past Events":
            return queryset.filter(event_date__lt=datetime.now())
        elif self.value()=="Upcoming Events":
            return queryset.filter(event_date__gt=datetime.now())
        elif self.value()=="Today Events":
            return queryset.filter(event_date__exact=datetime.now())
class NbeParticipantFilter(admin.SimpleListFilter):
    
    title="Nombre Des Participants"
    parameter_name = "nbe_participant"
    
    def lookups(self, request, model_admin):
        nb = 5
        return (
            (f"less than {nb}", (f"less than {nb}")),
            (f"more than {nb}", (f"more than {nb}")),
            ("0", ("0")),
        )
    def queryset(self, request, queryset):
        nb = 5
        if self.value()==f"less than {nb}":
            return queryset.filter(nbe_participant__lt=nb)
        elif self.value()==f"more than {nb}":
            return queryset.filter(nbe_participant__gt=nb)
        elif self.value()=="0":
            return queryset.filter(nbe_participant__exact=nb)
def set_True(ModelAdmin, request, queryset):
    req = queryset.update(state = True)
    if req==1:
        message = "1 event was "
    else:
        message = f"{req} events were "
    messages.success(request, message = "%ssuccessfully accepted"%message)
set_True.short_description = "Accept"
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def set_False(self, request, queryset):
        req = queryset.filter(state = False)
        if req.count()>0 :
            messages.error(request, f"{req.count()} events are already marked False")
        else:
            req = queryset.update(state = False)
            if req==1:
                message = "1 event was "
            else:
                message = f"{req} events were "
            messages.success(request, message = "%ssuccessfully marked rejected"%message)
    set_False.short_description = "Reject"
    list_display=(
        'title', 
        'description',
        'nbe_participant',
        'category',
        'state',
        'evt_participation',
        'creation_date',
        'event_date'
    )
    def evt_participation(self, obj):
        return obj.participation.count()
    actions=[set_True, set_False]
    list_per_page=2
    list_filter=('title', DateListFilter, NbeParticipantFilter)
    fieldsets = [
        ('A propos', {
            'fields':(
                'title', 'description'
            )
        }),
        (
            'Date',{
                'fields':('event_date','creation_date','update_date')
            }
        ),
        (
            'Other',{
                'fields':('category','state','nbe_participant')
            }
        ),
        (
            'Personal',{
                'fields':('organizer',)
            }
        )
    ]
    readonly_fields=('creation_date','update_date')
    inlines=(ParticipationsAdmin,)
    autocomplete_fields = ['organizer']


    

# admin.site.register(Event, EventAdmin)
<<<<<<< HEAD
# admin.site.register(Person)
=======
# admin.site.register(Person)
# #autocomplete_fields=['organizer']
#list_per_page=2
# admin.site.register(Event,EventAdmin) lier event lel admin 22
=======
from django.contrib import admin
from.models import *
# Register your models here.

class ParticipationAdmin(admin.TabularInline):
    model=Event_Participation
    extra=1



@admin.register(Event) 
class EventAdmin(admin.ModelAdmin):
    list_display=('title','description','nbe_participant','state','event_date','update_date','organizer')
# admin.site.register(Event,EventAdmin)
    list_per_page=2
    list_filter=('title','event_date','nbe_participant')
    fieldsets=[
        ('A propos', {
        "fields":(
        'title',
        'description',
        'image',
        'state'
        )
        }),
        ('Date',{
        "fields":(
        "event_date",
        "creation_date",
        "update_date",
        )
        }),
        ('Personnel',{
        "fields":(
        "organizer",
        )
        })
    ]
    readonly_fields=["creation_date","update_date"]
    inlines=(ParticipationAdmin,)
    autocomplete_fields = ['organizer']
>>>>>>> 3ed9813b3c5878d7b5d3f7df95dcb9e91e62ae72
>>>>>>> 3ab9d94c055339275ba825dfc462c43b16398c1a
