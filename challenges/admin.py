from django.contrib import admin
from challenges.models import Challenge, Run, Profil
from django.contrib.auth.models import User

admin.site.register(Challenge)
admin.site.register(Run)
admin.site.register(Profil)
