from django.contrib import admin
from .models import Poll , Choice , Response
class ChoiceInline(admin.TabularInline):
	model = Choice
class PollAdmin (admin. ModelAdmin ):
	list_display = ('name' ,'category', 'question' , "choice_count")
	inlines = [ChoiceInline,]

admin.site.register(Poll , PollAdmin)
class ChoiceAdmin (admin. ModelAdmin ):
	list_display = ("label" , "poll_name")
	raw_id_fields = ('poll', )
admin.site.register(Choice , ChoiceAdmin)

class ResponseAdmin (admin. ModelAdmin ):
	list_display = ('poll_name',"poll_category" , 'choice_label', 'comment')
admin.site.register(Response , ResponseAdmin)
# Register your models here.
