from django.urls import path
from .views import PlayerDataList, PlayerDataByTeamList, PlayerDataBySeasonList, PlayerDataByNameList

urlpatterns = [
    path('api/playerdata/', PlayerDataList.as_view(), name='playerdata_list'),
    path('api/playerdata/team/<str:team>/', PlayerDataByTeamList.as_view(), name='playerdata_by_team'),
    path('api/playerdata/season/<str:season>/', PlayerDataBySeasonList.as_view(), name='playerdata_by_season'),
    path('api/playerdata/name/<str:name>/', PlayerDataByNameList.as_view(), name='playerdata_by_name'),
]