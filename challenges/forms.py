from django import forms
import datetime

class AuthForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",max_length=30)
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)

class AddRunForm(forms.Form):
    date = forms.DateField(label="Date",widget=forms.SelectDateWidget, initial=datetime.date.today())
    score= forms.IntegerField(label="Score")
 
