from django.urls import path
from .views import add_players,add_teams,TeamsAPI,PlayersAPI,TransfersAPI,TransferMarketAPI

urlpatterns = [
    path('add_players',add_players.as_view(),name='add_players'),
    path('add_teams',add_teams.as_view(),name='add_teams'),
    path('api/teams',TeamsAPI.as_view(),name='teams_api'),
    path('api/teams/id=<int:pk>',TeamsAPI.as_view(),name='teams_api_by_id'),
    path('api/players',PlayersAPI.as_view(),name='players_api'),
    path('api/players/position=<int:pos>',PlayersAPI.as_view(),name='players_api_by_position'),
    path('api/players/id=<int:id>',PlayersAPI.as_view(),name='players_api_by_id'),
    path('api/players/team=<int:team>',PlayersAPI.as_view(),name='players_api_by_team'),
    path('api/transfermarket',TransferMarketAPI.as_view(),name='transfermarket_api'),
    path('api/transfermarket/player_id=<int:id>',TransferMarketAPI.as_view(),name='transfermarket_api_by_player_id'),
    path('api/transfermarket/seller_id=<int:seller_id>',TransferMarketAPI.as_view(),name='transfermarketapi_by_seller_id'),
    path('api/transfermarket/id=<int:id>',TransferMarketAPI.as_view(),name='transfermarketapi_by_id'),
    path('api/transfer',TransfersAPI.as_view(),name='transfers_api'),
    path('api/transfer/seller_id=<int:seller_id>',TransfersAPI.as_view(),name='transfers_api_by_seller_id'),
    path('api/transfer/buyer_id=<int:buyer_id>',TransfersAPI.as_view(),name='transfers_api_by_buyer_id'),
    path('api/transfer/id=<int:id>',TransfersAPI.as_view(),name='transfers_api_by_id'),
    path('api/transfer/player_id=<int:player_id>',TransfersAPI.as_view(),name='transfers_api_by_player_id'),

]