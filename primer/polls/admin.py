from django.contrib import admin
from .models import Question, Choice
# Register your models here
class CamposaFiltrar(admin.ModelAdmin): 
	list_filter = ['question','votes']

admin.site.register(Choice,CamposaFiltrar)

admin.site.register(Question)


