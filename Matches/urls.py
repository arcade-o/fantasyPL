from django.urls import path
from .views import add_matches,MatchAPI

urlpatterns=[
    path('add_match/<int:pk>',add_matches.as_view(),name='add_match'),
    path('api/matches',MatchAPI.as_view(),name='match_api'),
    path('api/matches/id=<int:id>',MatchAPI.as_view(),name='match_api_by_id'),
    path('api/matches/gameweek=<int:gameweek>',MatchAPI.as_view(),name='match_api_by_gameweek'),
    path('api/mathces/<int:hometeam>vs<int:awayteam>', MatchAPI.as_view(),name='match_api_by_home_vs_away')

]