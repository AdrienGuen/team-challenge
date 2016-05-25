#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class Challenge(models.Model):
    name = models.CharField(max_length=30)
    start_date = models.DateField(auto_now_add=True, auto_now=False, 
                                verbose_name="Starting date")
    goal = models.IntegerField()
    unite = models.CharField(max_length=30,default="")
    goal_date = models.DateField(auto_now_add=False, auto_now=False, 
                                verbose_name="Goal date")
    photo=models.ImageField(upload_to="photos/",default="dial.jpg");
    team = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Run(models.Model):
    date = models.DateField(auto_now_add=False, auto_now=False, 
                                verbose_name="Run date")
    user=models.ForeignKey(User)
    challenge = models.ForeignKey(Challenge)
    score = models.IntegerField(default=0)

    def __str__(self):
    	return "Run de {0}".format(self.user.username)

class Profil(models.Model):
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modele User
    challenge_list = models.ManyToManyField(Challenge)

    def __str__(self):
    	return "Profil de {0}".format(self.user.username)






from django.dispatch import receiver

@receiver(post_save, sender=User)
def ajout_profil(sender, instance,created, **kwargs):
	if(created): #si l utilisateur vient d etre cree
		profil = Profil(user=instance)
		profil.save();
