#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from models import Challenge,Profil,Run
from forms import AuthForm, AddRunForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render_to_response 
from chartit import DataPool, Chart


def connexion(request):
    """ Connexion page """
	 
    error=False
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = AuthForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
	    user=authenticate(username=username,password=password)
	    if user:
		login(request,user);
	    	return redirect(home)
	    else:
		error=True



    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = AuthForm()  # Nous créons un formulaire vide

    return render(request, 'challenges/connexion.html',locals())

def deconnexion(request):
   logout(request)
   return redirect(reverse(connexion))

@login_required
def home(request):
  
   """ Afficher tous les challenges """
   challenges = Challenge.objects.all() # Nous sélectionnons tous les challenges
   return render(request, 'challenges/chal.html', {'challenges': challenges})

@login_required
def mes_challenges(request):
    profil_user=Profil.objects.get(user=request.user)
    return render(request, 'challenges/mesChallenges.html', {'profil':profil_user})

@login_required
def afficher_challenge(request, id):
    error=False
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = AddRunForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            date = form.cleaned_data['date']
	    score=form.cleaned_data['score']
	    user=request.user
	    challenge = get_object_or_404(Challenge, id=id)
	    run=Run(date=date,score=score,challenge=challenge,user=user)
	    run.save()
	    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CREATION RUN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = AddRunForm()  # Nous créons un formulaire vide

    challenge = get_object_or_404(Challenge, id=id)  
    member=challenge.team.filter(id=request.user.id).exists()


    #Creation du graphique
    #Create the data

    #Voir highcharts pour les options
 
    series=[]
    series_options_terms={}
    for joueur in challenge.team.all():
	serie_joueur=	{'options': {'source': Run.objects.filter(user=joueur,challenge=challenge)}}
	serie_joueur['terms']=[{''.join(["score_",joueur.username]):'score'},{''.join(["date_",joueur.username]):'date'}]
	series.append(serie_joueur)
	series_options_terms[''.join(["date_",joueur.username])]=[''.join(["score_",joueur.username])]

    #Ajouter l'objectif
    serie_obj=	{'options': {'source': Challenge.objects.filter(id=challenge.id),'colors': 'red'},'terms':['goal_date','goal']}
    series_options_terms['goal_date']=['goal']
    series.append(serie_obj)

    

    challengeData =DataPool(series)

    print(series_options_terms)
    #Step 2: Create the Chart object

    series_options0 =[{'options':{
                  'type': 'spline',
                  'stacking': False},
                'terms':series_options_terms
		}]

    cht = Chart(
            datasource = challengeData,
            series_options=series_options0,
            chart_options =
              {'title': {'text': 'Performances'},
               'xAxis': {'title': {'text': 'Date'}},
	       'yAxis': {'title': {'text': 'Scores'}}
	})
 

    return render(request, 'challenges/challenge_page.html', locals())


@login_required
def rejoindre(request, id):
    challenge = get_object_or_404(Challenge, id=id)
    profil_user=Profil.objects.get(user=request.user)
    profil_user.challenge_list.add(challenge)
    challenge.team.add(request.user)
    return afficher_challenge(request,id)


@login_required
def quitter_challenge(request, id):
    challenge = get_object_or_404(Challenge, id=id)
    profil_user=Profil.objects.get(user=request.user)
    profil_user.challenge_list.remove(challenge)
    challenge.team.remove(request.user)
    return afficher_challenge(request,id)






