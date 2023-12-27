from django.contrib import admin
from .models import Attachment

# Register your models here.
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('task','file','description')

admin.site.register(Attachment, AttachmentAdmin)