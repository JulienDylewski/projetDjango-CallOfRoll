from django.contrib import admin

# Register your models here.
from .models import Student, Cursus, Presence

class StudentAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "email", "phone","cursus")
  #fields = ["first_name","last_name","birth_date","email","phone","comments","cursus"]
  fieldsets = [
    ('main', {'fields':['first_name','last_name',"birth_date"],'classes':['collapse']}),
    ('data', {'fields': ["email","phone","comments","cursus"],'classes':['collapse']})
  ]

class CursusAdmin(admin.ModelAdmin):
  list_display = ("name", "scholar_year")

class PresenceAdmin(admin.ModelAdmin):
  list_display = ("date", "cursus", "isMissing", "reason")


admin.site.register(Student, StudentAdmin)
admin.site.register(Cursus, CursusAdmin)
admin.site.register(Presence, PresenceAdmin)

