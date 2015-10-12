from django.contrib import admin
from .models import Poll , Choice , Response
class ChoiceInline(admin.TabularInline):
	model = Choice
class PollAdmin (admin. ModelAdmin ):
	list_display = ('name' ,'category', 'question')
	inlines = [ChoiceInline,]

admin.site.register(Poll , PollAdmin)
admin.site.register(Choice)
admin.site.register(Response)
# Register your models here.
