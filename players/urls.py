from django.urls import path
from .views import Heads, PlayerSearch, TeamDetail, PlayerByTeam, HeadById, Teams, PlayerList, PlayerDetail, PlayerByShortName, PlayersByCountry, PlayerByRole, PlayerByCountryRole, Categories, PlayerByCategory

urlpatterns = [
    path('heads/<int:id>/', HeadById.as_view(), name='head'),
    path('heads/', Heads.as_view(), name='heads'),
    path('teams/', Teams.as_view(), name='teams'),
    path('team/<int:id>', TeamDetail.as_view(), name='team_detail'),
    path('teams/<int:id>/', PlayerByTeam.as_view(), name='player_by_teams'),
    path('categories/', Categories.as_view(), name='categories'),
    path('players/', PlayerList.as_view(), name='players_list'),
    path('players/search/', PlayerSearch.as_view(), name='player_search'),
    path('categories/<int:id>', PlayerByCategory.as_view(), name='categories'),
    path('players/<int:id>/', PlayerDetail.as_view(), name='player_detail'),
    path('players/short_name/<str:short_name>/', PlayerByShortName.as_view(), name='player_by_short_name'),
    path('players/country/<str:country>/', PlayersByCountry.as_view(), name='players_by_country'),
    path('players/role/<str:role>/', PlayerByRole.as_view(), name='player_by_role'), 
    path('players/country_role/<str:country>/<str:role>/', PlayerByCountryRole.as_view(), name='player_by_country_role'),
]
