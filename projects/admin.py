from django.contrib import admin
from .models import Project, Detail, Text
admin.site.register(Text)

class DetailInline(admin.StackedInline): # new
    model = Detail
    extra = 0
class ProjectAdmin(admin.ModelAdmin): # new
    inlines = [
        DetailInline,
    ]   


admin.site.register(Project, ProjectAdmin)
admin.site.register(Detail)
