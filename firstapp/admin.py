from django.contrib import admin
from .models import *
# Register your models here.

all_models = [PersonalDetails,SmokingHabits, AlcoholHabits,GeneticRisk,
		 ChronicConditions,Obesity,Fatigue,Lifestyle,OtherSymptons]

for i in all_models:
	admin.site.register(i)