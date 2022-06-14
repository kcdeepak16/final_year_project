from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login

# Create your views here.

forms = {1:PersonalDetailsForm(),2:SmokingHabitsForm(), 3:AlcoholHabitsForm(),4:GeneticRiskForm(),
		 5:ChronicConditionsForm(),6:ObesityForm(),7:FatigueForm(),8:LifestyleForm(),9:OtherSymptonsForm()}

all_models = [PersonalDetails,SmokingHabits, AlcoholHabits,GeneticRisk,
		 ChronicConditions,Obesity,Fatigue,Lifestyle,OtherSymptons]


cluster_dict = {'age': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1,
                        15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1,
                        29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 2, 42: 2, 
                        43: 2, 44: 2, 45: 2, 46: 2, 47: 2, 48: 2, 49: 2, 50: 2, 51: 2, 52: 2, 53: 2, 54: 2, 55: 2, 56: 2, 
                        57: 2, 58: 2, 59: 2, 60: 2, 61: 3, 62: 3, 63: 3, 64: 3, 65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 
                        71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 2, 77: 2, 78: 2, 79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 
                        85: 2, 86: 2, 87: 2, 88: 2, 89: 2, 90: 2}, 
                'gender': {'Female': 1, 'Male': 2}, 
                'smoking Habits': {'Past Smoker': 2.5, 'Active': 3, 'Passive': 2, 'Non-Smoker': 1}, 
                'Smoking':{0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2, 11: 3, 12: 3, 13: 3, 14: 3, 
                           15: 3, 16: 4, 17: 4, 18: 4, 19: 4, 20: 4, 21: 4, 22: 4, 23: 4, 24: 4, 25: 4, 26: 4, 27: 4, 28: 4, 
                           29: 4, 30: 4, 31: 5, 32: 5, 33: 5, 34: 5, 35: 5, 36: 5, 37: 5, 38: 5, 39: 5, 40: 5, 41: 5, 42: 5,
                           43: 5, 44: 5, 45: 5, 46: 5, 47: 5, 48: 5, 49: 5, 50: 5, 51: 5, 52: 5, 53: 5, 54: 5, 55: 5, 56: 5, 
                           57: 5, 58: 5, 59: 5, 60: 5, 61: 5, 62: 5, 63: 5, 64: 5, 65: 5, 66: 5, 67: 5, 68: 5, 69: 5, 70: 5, 
                           71: 5, 72: 5, 73: 5, 74: 5, 75: 5, 76: 5, 77: 5, 78: 5, 79: 5, 80: 5, 81: 5, 82: 5, 83: 5, 84: 5, 
                           85: 5, 86: 5, 87: 5, 88: 5, 89: 5, 90: 5},
                'alcohol': {'Weekly': 1.5, 'Occasionally': 1, 'Non Drinker': 1, 'Daily': 3},
                'genetic risk': {'Parent': 3, 'Other Relative': 2, 'No Risk': 1}, 
                'chronic lung diseases': {'Yes': 2, 'No': 1}, 
                'obesity': {'Yes': 2, 'No': 1}, 
                'Frequent chest pain': {'Yes': 2, 'No': 1}, 
                'fatigue': {'Yes': 2, 'No': 1}, 
                'weight loss': {'Yes': 2, 'No': 1}, 
                'Chronic cold and Cough': {'Yes': 2, 'No': 1}, 
                'physical activity Times/Week': {0: 3, 1: 3, 2: 2, 3: 2, 4: 2, 5: 1, 6: 1, 7: 1}}


severity_fact = {'smoking Habits': 2.5980233486545394,
 'alcohol': 1.132699822573447,
 'chronic lung diseases': 2.4285678667597486,
 'obesity': 1.0574868906583803,
 'Frequent chest pain': 1.705360803608036,
 'fatigue': 1.0686588833101447,
 'weight loss': 0.8994133106798694,
 'Chronic cold and Cough': 1.1162361623616237,
 'physical activity Times/Week': 1.0207685958438533,
 'age': {0: 0.0,
  1: 0.0,
  2: 0.0,
  3: 0.0,
  4: 0.0,
  5: 0.0,
  6: 0.0,
  7: 0.0,
  8: 0.0,
  9: 0.0,
  10: 0.0,
  11: 0.0,
  12: 0.0,
  13: 0.0,
  14: 0.0,
  15: 0.0,
  16: 0.0,
  17: 0.0,
  18: 0.0,
  19: 0.0,
  20: 0.0,
  21: 0.0,
  22: 0.0,
  23: 0.0,
  24: 0.0,
  25: 0.0,
  26: 0.0,
  27: 0.0,
  28: 0.0,
  29: 0.0,
  31: 0.03916618113549556,
  32: 0.03916618113549556,
  33: 0.03916618113549556,
  34: 0.03916618113549556,
  35: 0.03916618113549556,
  36: 0.03916618113549556,
  37: 0.03916618113549556,
  38: 0.03916618113549556,
  39: 0.03916618113549556,
  41: 0.44649446494464945,
  42: 0.44649446494464945,
  43: 0.44649446494464945,
  44: 0.44649446494464945,
  45: 0.44649446494464945,
  46: 0.44649446494464945,
  47: 0.44649446494464945,
  48: 0.44649446494464945,
  49: 0.44649446494464945,
  51: 1.4039258949290523,
  52: 1.4039258949290523,
  53: 1.4039258949290523,
  54: 1.4039258949290523,
  55: 1.4039258949290523,
  56: 1.4039258949290523,
  57: 1.4039258949290523,
  58: 1.4039258949290523,
  59: 1.4039258949290523,
  61: 3.384716105225568,
  62: 3.384716105225568,
  63: 3.384716105225568,
  64: 3.384716105225568,
  65: 3.384716105225568,
  66: 3.384716105225568,
  67: 3.384716105225568,
  68: 3.384716105225568,
  69: 3.384716105225568,
  71: 4.544675803900897,
  72: 4.544675803900897,
  73: 4.544675803900897,
  74: 4.544675803900897,
  75: 4.544675803900897,
  76: 4.544675803900897,
  77: 4.544675803900897,
  78: 4.544675803900897,
  79: 4.544675803900897,
  81: 1.0574868906583808,
  82: 1.0574868906583808,
  83: 1.0574868906583808,
  84: 1.0574868906583808,
  85: 1.0574868906583808,
  86: 1.0574868906583808,
  87: 1.0574868906583808,
  88: 1.0574868906583808,
  89: 1.0574868906583808},
 'genetic risk': {'No Risk': 0.8549894009578393,
  'Other Relative': 0.9874396820891286,
  'Parent': 1.4138991389913897},
 'Smoking':3.3810349278329923
 }

percentage_values = {'Age': {(0, 30): 0.0,
							  (31, 40): 0.007380073800738007,
							  (41, 50): 0.11070110701107011,
							  (51, 60): 0.22509225092250923,
							  (61, 70): 0.34686346863468637,
							  (71, 80): 0.21033210332103322,
							  (81, 90): 0.0996309963099631},
					 'Gender': {'Male': 0.6531365313653137, 
					 			'Female': 0.34686346863468637},
					 'Smoking Habits': {'Past Smoker': 0.3874538745387454,
										'Active': 0.72,
										'Non-Smoker': 0.14022140221402213,
										'Passive': 0.12546125461254612},
					 'Smoking Duration': {0: 0.2656826568265683,
											 1: 0.2878228782287823,
											 2: 0.31365313653136534,
											 3: 0.33579335793357934,
											 4: 0.35424354243542433,
											 5: 0.3874538745387454,
											 6: 0.41697416974169743,
											 7: 0.43911439114391143,
											 8: 0.46863468634686345,
											 9: 0.4944649446494465,
											 10: 0.5350553505535055,
											 11: 0.5940959409594095,
											 12: 0.6236162361623616,
											 13: 0.6605166051660517,
											 14: 0.7011070110701108,
											 15: 0.7380073800738007,
											 16: 0.7822878228782287,
											 17: 0.8413284132841329,
											 18: 0.8745387453874539,
											 19: 0.933579335793358,
											 20: 0.959409594095941,
											 21: 0.9630996309963099,
											 22: 0.9704797047970479,
											 23: 0.981549815498155,
											 26: 0.985239852398524,
											 27: 0.992619926199262,
											 29: 0.996309963099631,
											 32: 1.0,
											 24: 0.981549815498155,
											 25: 0.981549815498155,
											 28: 0.992619926199262,
											 30: 0.996309963099631,
											 31: 0.996309963099631},
					 'Smoking Frequency': {0: 0.2656826568265683,
					 					   1: 0.21033210332103322,
					 					   2: 0.23247232472324722,
					 					   3: 0.2915129151291513,
										   },
					 'Alcohol Intake': {'Non Drinker': 0.36531365313653136,
								  'Daily': 0.63,
								  'Weekly': 0.19557195571955718,
								  'Occasionally': 0.18081180811808117},
					 'Genetic Risk': {'No Risk': 0.46494464944649444,
									  'Parent': 0.31,
									  'Other Relative': 0.25461254612546125},
					 'Chronic Lung Diseases': {'Yes': 0.5940959409594095, 'No': 0.4059040590405904},
					 'Obesity': {'No': 0.6678966789667896, 'Yes': 0.33210332103321033},
					 'Frequent Chest Pain': {'Yes': 0.6088560885608856, 'No': 0.39114391143911437},
					 'Fatigue': {'Yes': 0.5387453874538746, 'No': 0.4612546125461255},
					 'Weight Loss': {'No': 0.7933579335793358, 'Yes': 0.2066420664206642},
					 'Chronic Cold and Cough': {'No': 0.6568265682656826, 'Yes': 0.34317343173431736},
					 'Physical Activity': {
													  0: 0.1881918819188192,
													  1: 0.16605166051660517,
													  2: 0.14391143911439114,
													  3: 0.2029520295202952,
													  4: 0.12546125461254612,
													  5: 0.08118081180811808,
													  6: 0.033210332103321034,
													  7: 0.05904059040590406}
					}

edit_forms = {1:PersonalDetailsForm,2:SmokingHabitsForm, 3:AlcoholHabitsForm,4:GeneticRiskForm,
		 5:ChronicConditionsForm,6:ObesityForm,7:FatigueForm,8:LifestyleForm,9:OtherSymptonsForm}

def serialize_form(request, num):
	if num == 2:
		return SmokingHabitsForm(request.POST)
	elif num == 3:
		return AlcoholHabitsForm(request.POST)
	elif num == 4:
		return GeneticRiskForm(request.POST)
	elif num == 5:
		return ChronicConditionsForm(request.POST)
	elif num == 6:
		return ObesityForm(request.POST)
	elif num == 7:
		return FatigueForm(request.POST)
	elif num == 8:
		return LifestyleForm(request.POST)
	elif num == 9:
		return OtherSymptonsForm(request.POST)


def index(request, num):
	if request.method == "POST":
		if num == 1:
			new_user = User()
			new_user.first_name = request.POST.get("first_name")
			new_user.last_name = request.POST.get("last_name")
			new_user.username = request.POST.get("email")
			new_user.email = request.POST.get("email")
			new_user.save()	
			form_serializer = PersonalDetailsForm(data=request.POST)
			if form_serializer.is_valid():
				new_user_form = form_serializer.save()
				new_user_form.user = new_user
				new_user_form.save()
				login(request, new_user)
				return HttpResponseRedirect(f"/form/{num+1}") 
		else:
			form_serializer = serialize_form(request,num)
			if form_serializer.is_valid():
				saved_form = form_serializer.save()
				saved_form.user = request.user
				saved_form.save()
				if num == 9:
					return HttpResponseRedirect("/result")
				return HttpResponseRedirect(f"/form/{num+1}") 

	c=1
	if request.user.is_authenticated:
		for i in all_models:
			if i.objects.filter(user=request.user).exists():
				c+=1
			else:
				break
	if c == 10:
		return HttpResponseRedirect("/result")
	if num == c:
		return render(request, 'index.html', {'form':forms[c]})
	return HttpResponseRedirect(f"/form/{c}") 


def edit_form(request, num):
	if request.method == "POST":
		form_data = edit_forms[num](instance=all_models[num-1].objects.get(user=request.user), data=request.POST)
		if form_data.is_valid():
			form_data.save()
			return HttpResponseRedirect(f"/form/1")
	if all_models[num-1].objects.filter(user=request.user).exists():
		return render(request, 'index.html', {'form':edit_forms[num](instance=all_models[num-1].objects.get(user=request.user))})
	else:
		print("Hi")
		return HttpResponseRedirect(f"/form/1") 



class UserReport:
	def __init__(self, user):
		self.user = user
		self.pdobj = PersonalDetails.objects.get(user=user)
		self.smobj = SmokingHabits.objects.get(user=user)
		self.alobj = AlcoholHabits.objects.get(user=user)
		self.grobj = GeneticRisk.objects.get(user=user)
		self.ccobj = ChronicConditions.objects.get(user=user)
		self.obobj = Obesity.objects.get(user=user)
		self.faobj = Fatigue.objects.get(user=user)
		self.lfobj = Lifestyle.objects.get(user=user)
		self.osobj = OtherSymptons.objects.get(user=user)

	def AgeScore(self):
		return cluster_dict['age'][self.pdobj.age]*severity_fact['age'][self.pdobj.age]

	def GenderScore(self):
		return cluster_dict['gender'][self.pdobj.gender]

	def SmokingHabitsScore(self):
		return cluster_dict['smoking Habits'][self.smobj.current_smoking_habits]*severity_fact['smoking Habits']

	def SmokingDuration(self):
		if self.smobj.current_smoking_habits in ["Active","Past Smoker"]:
			cs = self.smobj.years_smoked*self.smobj.average_pack
			return cluster_dict["Smoking"][cs]*severity_fact["Smoking"]
		else:
			return 0

	def AlcoholScore(self):
		return cluster_dict["alcohol"][self.alobj.alcohol_habits]*severity_fact["alcohol"]

	def GeneticRiskScore(self):
		return cluster_dict["genetic risk"][self.grobj.risk_type]*severity_fact["genetic risk"][self.grobj.risk_type]

	def ChronicLungScore(self):
		return cluster_dict["chronic lung diseases"][self.ccobj.chronic_lung_diseases]*severity_fact["chronic lung diseases"]

	def ObesityScore(self):
		return cluster_dict["obesity"][self.obobj.is_obese()]*severity_fact["obesity"]

	def ChestPainScore(self):
		return cluster_dict["Frequent chest pain"][self.ccobj.frequent_chest_pain]*severity_fact["Frequent chest pain"]

	def FatigueScore(self):
		return cluster_dict["fatigue"][self.faobj.fatigue]*severity_fact["fatigue"]

	def WeightLossScore(self):
		return cluster_dict["weight loss"][self.lfobj.weight_loss]*severity_fact["weight loss"]

	def ChronicColdScore(self):
		return cluster_dict["Chronic cold and Cough"][self.ccobj.chronic_cold]*severity_fact["Chronic cold and Cough"]

	def PhysicalActivityScore(self):
		return cluster_dict["physical activity Times/Week"][self.lfobj.physical_activity]*severity_fact["physical activity Times/Week"]

	def PercentageScores(self):
		retrurn_percentage = {}
		curr_values = {'Age': self.pdobj.age,
					    'Gender': self.pdobj.gender,
					 	'Smoking Habits': self.smobj.current_smoking_habits,
					 	'Smoking Duration': self.smobj.years_smoked,
					 	'Smoking Frequency': self.smobj.average_pack,
					 	'Alcohol Intake': self.alobj.alcohol_habits,
					 	'Genetic Risk': self.grobj.risk_type,
					 	'Chronic Lung Diseases': self.ccobj.chronic_lung_diseases,
					 	'Obesity': self.obobj.is_obese(),
					 	'Frequent Chest Pain': self.ccobj.frequent_chest_pain,
					 	'Fatigue': self.faobj.fatigue,
					 	'Weight Loss': self.lfobj.weight_loss,
					 	'Chronic Cold and Cough': self.ccobj.chronic_cold,
					 	'Physical Activity': self.lfobj.physical_activity
					}
		for i, j in percentage_values.items():
			if i in ['Age', 'Smoking Frequency', 'Physical Activity']:
				if i in ['Age']:
					f=0
					for n in j.keys():
						if curr_values[i]>=n[0] and curr_values[i]<=n[1]:
							f+=j[n]
							break
						else:
							f+=j[n]
					curr_values[i]=f
				else:
					f=0
					for n in j.keys():
						if curr_values[i] == n:
							f+=j[n]
							break
						else:
							f+=j[n]
					if i == "Physical Activity":
						curr_values[i]=1-f
					else:
						curr_values[i]=f
			else:
				curr_values[i]=percentage_values[i][curr_values[i]]

		positives = {}
		negatives = {}
		messages = {'Age': f"%p1 % of Lung Cancer patients are {self.pdobj.age} years old or younger ",
					 'Gender': f"%p1 % of Lung Cancer patients are {self.pdobj.gender}",
					 'Smoking Habits': f"%p1 % of Lung Cancer patients are {'Active or Past Smoker' if self.smobj.current_smoking_habits == 'Active' else self.smobj.current_smoking_habits} Smokers",
					 'Smoking Duration': f"%p1 % of Lung Cancer patients have been smoking for {self.smobj.years_smoked} years or less",
					 'Smoking Frequency': f"%p1 % of Lung Cancer patients smoke on average {self.smobj.average_pack} number of packets each day",
					 'Alcohol Intake': f"%p1 % of Lung Cancer patients are {self.alobj.alcohol_habits} drinkers",
					 'Genetic Risk': f"%p1 % of Lung Cancer patients have a Genetic Risk of {self.grobj.risk_type}",
					 'Chronic Lung Diseases': f"%p1 % of Lung Cancer patients {'do not' if self.ccobj.chronic_lung_diseases == 'No' else ''} have Chronic Lung Diseases",
					 'Obesity': f"%p1 % of Lung Cancer patients {'are' if self.obobj.is_obese() == 'Yes' else 'are not'} obese",
					 'Frequent Chest Pain': f"%p1 % of Lung Cancer patients {'do not' if self.ccobj.frequent_chest_pain == 'Yes' else ''} have Frequent Chest Pain",
					 'Fatigue': f"%p1 % of Lung Cancer patients {'do not' if self.faobj.fatigue == 'No' else ''} have Fatigue",
					 'Weight Loss': f"%p1 % of Lung Cancer patients {'do not' if self.lfobj.weight_loss == 'No' else ''} have Weight Loss",
					 'Chronic Cold and Cough': f"%p1 % of Lung Cancer patients {'do not' if self.ccobj.chronic_cold == 'No' else ''} have Chronic Cold & Cough",
					 'Physical Activity': f"%p1 % of Lung Cancer patients work out {self.lfobj.physical_activity} times a week"
					}

		for i in curr_values:
			messages[i]=messages[i].replace("%p1", "%.2f" % (curr_values[i]*100))
		for i, j in curr_values.items():
			if j>0.5:
				negatives[i]=messages[i]
			else:
				positives[i]=messages[i]
		return {'positives':positives, 'negatives':negatives}

	def IndividualTotalScore(self):
		return [self.AgeScore(),self.GenderScore(),self.SmokingHabitsScore(),self.SmokingDuration(),self.AlcoholScore(),self.GeneticRiskScore(),self.ChronicLungScore(),self.ObesityScore(),self.ChestPainScore(),self.FatigueScore(),self.WeightLossScore(),self.ChronicColdScore(),self.PhysicalActivityScore()]

	def TotalScore(self):
		return self.AgeScore()+self.GenderScore()+self.SmokingHabitsScore()+self.SmokingDuration()+self.AlcoholScore()+self.GeneticRiskScore()+self.ChronicLungScore()+self.ObesityScore()+self.ChestPainScore()+self.FatigueScore()+self.WeightLossScore()+self.ChronicColdScore()+self.PhysicalActivityScore()



def result(request):
	ur = UserReport(request.user)
	ps = ur.PercentageScores()
	negatives, positives = ps['negatives'], ps['positives']
	print(ur.IndividualTotalScore())
	return render(request, "result.html", {'score':ur.TotalScore(), 'negatives':negatives, 'positives': positives})