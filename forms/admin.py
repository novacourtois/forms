from django.contrib import admin
from forms.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
     model = Choice
     extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date')
    
admin.site.register(Poll, PollAdmin)
