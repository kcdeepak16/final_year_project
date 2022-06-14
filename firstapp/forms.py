from django import forms 
from .models import *

class PersonalDetailsForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", max_length=50, 
                                widget=forms.TextInput(attrs={'hint':'Enter your first name here','col_class':'col-6'}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={'col_class':'col-6'}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.TextInput(attrs={'col_class':'col-6'}))
    phone_no = forms.IntegerField(label="Phone Number", widget=forms.TextInput(attrs={'col_class':'col-6'}))
    age = forms.IntegerField(label="Age", widget=forms.TextInput(attrs={'col_class':'col-6'}))
    gender = forms.ChoiceField(choices=(('Male','Male'), ('Female','Female')), widget=forms.Select(attrs={'col_class':'col-6'}))

    class Meta:
        model = PersonalDetails
        fields = ["first_name","last_name","email","phone_no","age","gender"]


class SmokingHabitsForm(forms.ModelForm):
    current_smoking_habits = forms.ChoiceField(choices=(('Active','Active'),('Passive','Passive'),
                                            ('Non-Smoker','Non-Smoker')), widget=forms.Select(attrs={'col_class':'col-6'}))
    years_smoked = forms.IntegerField(min_value=0, max_value=50, widget=forms.TextInput(attrs={'col_class':'col-6'}), required=False)
    average_pack = forms.IntegerField(min_value=0, widget=forms.TextInput(attrs={'col_class':'col-6'}), required=False)
    passive_intensity = forms.ChoiceField(choices=(('Low','Low'),('Medium','Medium'),('High','High')),
                                          widget=forms.Select(attrs={'col_class':'col-6'}), required=False)

    class Meta:
        model = SmokingHabits
        exclude = ('user',)


class AlcoholHabitsForm(forms.ModelForm):
    alcohol_habits = forms.ChoiceField(choices=(("Daily","Daily"),("Weekly","Weekly"),
                                                              ("Occassionally","Occassionally"),("Non Drinker","Non Drinker")),
                                                      widget=forms.Select(attrs={'col_class':'col-6'}))
    time_active = forms.IntegerField(min_value=0, widget=forms.TextInput(attrs={'col_class':'col-6'}))


    class Meta:
        model = AlcoholHabits
        exclude = ('user',)


class GeneticRiskForm(forms.ModelForm):
    risk_type = forms.ChoiceField(choices=(("Parent","Parent"),("Other Relative","Other Relative"),
                                            ("No Risk","No Risk")), widget=forms.Select(attrs={'col_class':'col-6'}))
    number_of_relatives = forms.IntegerField(validators=[MinValueValidator(0)], required=False,
                                            widget=forms.TextInput(attrs={'col_class':'col-6'}))

    class Meta:
        model = GeneticRisk
        exclude = ('user',)


class ChronicConditionsForm(forms.ModelForm):
    chronic_lung_diseases = forms.ChoiceField(choices=(("Yes","Yes"),("No","No")), widget=forms.Select(attrs={'col_class':'col-12'}))
    frequent_chest_pain = forms.ChoiceField(choices=(("Yes","Yes"),("No","No")), widget=forms.Select(attrs={'col_class':'col-12'}))
    chronic_cold = forms.ChoiceField(choices=(("Yes","Yes"),("No","No")), widget=forms.Select(attrs={'col_class':'col-12'}))

    class Meta:
        model = ChronicConditions
        exclude = ('user',)


class ObesityForm(forms.ModelForm):
    weight = forms.DecimalField(widget=forms.TextInput(attrs={'col_class':'col-6'}))
    height = forms.IntegerField(widget=forms.TextInput(attrs={'col_class':'col-6'}))
    bmi = forms.DecimalField(widget=forms.TextInput(attrs={'col_class':'col-6'}), disabled=True, required=False)

    class Meta:
        model = Obesity
        exclude = ('user',)


class FatigueForm(forms.ModelForm):
    fatigue = forms.ChoiceField(choices=(("Yes","Yes"),("No","No")), widget=forms.HiddenInput(), required=False)
    fatigue1 = forms.ChoiceField(choices=(("Yes","Yes"),("No","No")), 
                label="Do you get tired after walking for 10 minutes?", widget=forms.Select(attrs={'col_class':'col-12'}))
    fatigue2 = forms.ChoiceField(choices=(("Yes","Yes"),("No","No")), 
                label="Do you get tired after climbing a flight of stairs?", widget=forms.Select(attrs={'col_class':'col-12'}))
    fatigue3 = forms.ChoiceField(choices=(("Yes","Yes"),("No","No")), 
                label="Do you have any problems performing basic household chores?", widget=forms.Select(attrs={'col_class':'col-12'}))

    class Meta:
        model = Fatigue
        exclude = ('user',)

class LifestyleForm(forms.ModelForm):
    weight_loss = forms.ChoiceField(choices=(("Yes","Yes"),("No","No")), label="Have you been losing weight recently?",
                                    widget=forms.Select(attrs={'col_class':'col-12'}))
    physical_activity = forms.ChoiceField(choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)), label="How many times do you work out weekly?",
                                            widget=forms.Select(attrs={'col_class':'col-12'}))

    class Meta:
        model = Lifestyle
        exclude = ('user',)
    

class OtherSymptonsForm(forms.ModelForm):
    coughing_blood = forms.ChoiceField( choices=(("Yes","Yes"),("No","No")), widget=forms.Select(attrs={'col_class':'col-6'}))
    fatty_diet = forms.ChoiceField( choices=(("Yes","Yes"),("No","No")), widget=forms.Select(attrs={'col_class':'col-6'}))
    tobacco = forms.ChoiceField( choices=(("Yes","Yes"),("No","No")), widget=forms.Select(attrs={'col_class':'col-6'}))
    balance_problems = forms.ChoiceField( choices=(("Yes","Yes"),("No","No")), widget=forms.Select(attrs={'col_class':'col-6'}))
    heart_problems = forms.ChoiceField( choices=(("Yes","Yes"),("No","No")), widget=forms.Select(attrs={'col_class':'col-6'}))

    class Meta:
        model = OtherSymptons
        exclude = ('user',)