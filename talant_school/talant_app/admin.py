from django.contrib import admin
from .models import *

class ClubImageInline(admin.TabularInline):
    model = ClubImage
    extra = 1

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'is_active')
    list_filter = ('is_active',)
    inlines = [ClubImageInline]
    
admin.site.register(Slider)
admin.site.register(About)

admin.site.register(AdministrationMember)
admin.site.register(Registration)
admin.site.register(EducationLevel)
admin.site.register(News)
admin.site.register(Admission)
admin.site.register(FooterContact)
admin.site.register(StudentParliament)
admin.site.register(ParliamentActivity)
admin.site.register(Rule)
admin.site.register(Schedule)
admin.site.register(Accreditation)
admin.site.register(AccreditationDocument)