from django.contrib import admin
from .models import Player, Category, Team, Head

admin.site.register(Head)
admin.site.register(Player)
admin.site.register(Category)
admin.site.register(Team)