from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class PersonalDetails(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	phone_no = models.IntegerField()
	age = models.IntegerField()
	gender = models.CharField(max_length=10, choices=(('Male','Male'), ('Female','Female')))

class SmokingHabits(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	current_smoking_habits = models.CharField(max_length=20, choices=(('Active','Active'),('Passive','Passive'),
										('Past Smoker','Past Smoker'),('Non-Smoker','Non-Smoker')))
	years_smoked = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)],blank=True,null=True)
	average_pack = models.IntegerField(blank=True, null=True)
	passive_intensity = models.CharField(max_length=10, choices=(('Low','Low'),('Medium','Medium'),
										('High','High')), blank=True)


class AlcoholHabits(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	alcohol_habits = models.CharField(max_length=20, choices=(("Daily","Daily"),("Weekly","Weekly"),
															  ("Occassionally","Occassionally"),("Non Drinker","Non Drinker")))
	time_active = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)


class GeneticRisk(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	risk_type = models.CharField(max_length=20, choices=(("Parent","Parent"),("Other Relative","Other Relative"),
														 ("No Risk","No Risk")))
	number_of_relatives = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)


class ChronicConditions(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	chronic_lung_diseases = models.CharField(max_length=10, choices=(("Yes","Yes"),("No","No")))
	frequent_chest_pain = models.CharField(max_length=10, choices=(("Yes","Yes"),("No","No")))
	chronic_cold = models.CharField(max_length=10, choices=(("Yes","Yes"),("No","No")))


class Obesity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	weight = models.IntegerField()
	height = models.IntegerField()

	def is_obese(self):
		bmi = self.weight/(self.height/10)**2
		if bmi>25:
			return "Yes"
		else:
			return "No"

	def save(self, *args, **kwargs):
		print(self)
		super(Obesity, self).save(*args, **kwargs)


class Fatigue(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	fatigue = models.CharField(max_length = 10, choices=(("Yes","Yes"),("No","No")))

class Lifestyle(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	weight_loss = models.CharField(max_length = 10, choices=(("Yes","Yes"),("No","No")))
	physical_activity = models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)))


class OtherSymptons(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	coughing_blood = models.CharField(max_length = 10, choices=(("Yes","Yes"),("No","No")))
	fatty_diet = models.CharField(max_length = 10, choices=(("Yes","Yes"),("No","No")))
	tobacco = models.CharField(max_length = 10, choices=(("Yes","Yes"),("No","No")))
	balance_problems = models.CharField(max_length = 10, choices=(("Yes","Yes"),("No","No")))
	heart_problems = models.CharField(max_length = 10, choices=(("Yes","Yes"),("No","No")))