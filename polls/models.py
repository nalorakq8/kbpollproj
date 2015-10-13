#-*- coding: utf -8 -*-
from django.db import models

class Poll(models.Model):
	category_choices = (
		("Sports","Sports"),
		("Politics","Politics"),
		("Demographic","Demographic"),
		("Academics" , "Academics"),
		("Travel" , "Travel")
		)
	name = models. CharField ("poll name", max_length =64 )
	category = models. CharField ("poll category", max_length =64, choices = category_choices)
	question = models. TextField (blank=True)
	def __unicode__(self):
		return u"{}: {}".format(self.name , self.category)
	def choice_count (self):
		return self.choice_set.count()
	#challenge 1.5 part 7
	#becuase we didnt create new class we created a method and method dont need to be migrated in orded for it to be functional
class Choice(models.Model):
	poll = models. ForeignKey (Poll , verbose_name ="poll question")
	label = models. CharField ("answer choice", max_length =200)
	created_at = models. DateTimeField ( auto_now_add =True)
	updated_at = models. DateTimeField ("last updated", auto_now=True)
	def poll_name(self):
		return self.poll.name
	

class Response(models.Model):
	choice = models. ForeignKey (Choice , null=True , blank=True)
	comment = models. TextField (blank=True)
	submitted_at = models. DateTimeField ( auto_now_add =True)
	def poll_name(self):
		return self.choice.poll.name
	def choice_label(self):
		return self.choice.label
	def poll_category(self):
		return self.choice.poll.category
