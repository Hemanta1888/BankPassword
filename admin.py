from django.contrib import admin
from .models import question_form

class question_form_admin(admin.ModelAdmin):
    list_display = ['questions','opt1','opt2','opt3','opt4']
    list_display_links = ['questions']
    
admin.site.register(question_form,question_form_admin)
