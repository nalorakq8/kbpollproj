from django.contrib import admin
from .models import Poll , Choice , Response
class PollAdmin (admin. ModelAdmin ):
	list_display = ('name' ,'category', 'question')

admin.site.register(Poll , PollAdmin)
admin.site.register(Choice)
admin.site.register(Response)
# Register your models here.
