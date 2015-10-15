from django.contrib import admin
from .models import Poll , Choice , Response
class ChoiceInline(admin.StackedInline):
	model = Choice
class ResponseInline(admin.TabularInline):
	model = Response
class PollAdmin (admin. ModelAdmin ):
	list_display = ('name' ,'category', 'question' , "choice_count")
	list_filter = ("category",)
	search_fields = ["name", "question"]
	inlines = [ChoiceInline,ResponseInline,]

admin.site.register(Poll , PollAdmin)
class ChoiceAdmin (admin. ModelAdmin ):
	raw_id_fields = ('poll', )
	list_display = ("label" , "poll_name")
	
admin.site.register(Choice , ChoiceAdmin)

class ResponseAdmin (admin. ModelAdmin ):
	list_display = ('poll_name',"poll_category" , 'choice_label', 'comment')
admin.site.register(Response , ResponseAdmin)
# Register your models here.
