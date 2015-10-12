from django.contrib import admin
from .models import Poll , Choice , Response
class ChoiceInline(admin.TabularInline):
	model = Choice
class PollAdmin (admin. ModelAdmin ):
	list_display = ('name' ,'category', 'question' , "choice_count")
	inlines = [ChoiceInline,]

admin.site.register(Poll , PollAdmin)
admin.site.register(Choice)
class ResponseAdmin (admin. ModelAdmin ):
	list_display = ('poll_name', 'choice_label', 'comment')
admin.site.register(Response , ResponseAdmin)
# Register your models here.
