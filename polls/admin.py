from django.contrib import admin
from .models import Poll , Choice , Response , UserProfile , Survey
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
class ChoiceInline(admin.StackedInline):
	model = Choice
class ResponseInline(admin.TabularInline):
	model = Response
class UserProfileInline(admin.StackedInline):
	model = UserProfile
class PollAdmin (admin. ModelAdmin ):
	list_display = ('name' ,'category', 'question' , "choice_count")
	list_filter = ("category",)
	search_fields = ["name", "question"]
	inlines = [ChoiceInline,ResponseInline,]
class ChoiceAdmin (admin. ModelAdmin ):
	raw_id_fields = ('poll', )
	list_display = ("label" , "poll_name")
	
class ResponseAdmin (admin. ModelAdmin ):
	list_display = ('poll_name',"poll_category" , 'choice_label', 'comment')

class UserAdmin(UserAdmin):
	inlines = (UserProfileInline,)

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user' , 'gender' , 'bio' , 'location' , 'phone')

class SurveyAdmin(admin.ModelAdmin):
	list_display = ('name' ,)
#Challenge 3.5 part 3
#we use through in many to many relationship to specify the intermediat table and its used when you want to associate extra data

admin.site.register(Poll , PollAdmin)
admin.site.register(Choice , ChoiceAdmin)
admin.site.register(Response , ResponseAdmin)
admin.site.register(Survey , SurveyAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

