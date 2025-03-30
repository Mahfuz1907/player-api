from django.urls import path
from .views import PlayerList, PlayerDetail, PlayerByShortName, PlayersByTeam, PlayerByRole, PlayerByTeamRole, PlayerByCategory

urlpatterns = [
    path('players/', PlayerList.as_view(), name='players_list'),
    path('players/<int:id>/', PlayerDetail.as_view(), name='player_detail'),
    path('players/short_name/<str:short_name>/', PlayerByShortName.as_view(), name='player_by_short_name'),
    path('players/team/<str:team>/', PlayersByTeam.as_view(), name='players_by_team'),
    path('players/role/<str:role>/', PlayerByRole.as_view(), name='player_by_role'), 
    path('players/team_role/<str:team>/<str:role>/', PlayerByTeamRole.as_view(), name='player_by_team_role'),
    path('players/category/<str:category>/', PlayerByCategory.as_view(), name='player_by_category'),
]
