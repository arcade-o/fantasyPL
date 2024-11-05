from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
import json
import urllib
from .models import Match
from rest_framework import generics
from .serializers import MatchSerializer



# Create your views here.

#add matches from fantasypl api

class add_matches(UserPassesTestMixin,View):
    def test_func(self):
        return self.request.user.is_superuser
    
    def get(self,request,pk):
        base_url = 'https://fantasy.premierleague.com/api/fixtures/'
        data = json.loads(urllib.request.urlopen(base_url).read())
        for entry in data:
            if entry['event'] == pk:
                if Match.objects.filter(id=entry['id']).exists():
                    pass
                else:
                    match = Match(
                        gameweek = entry['event'],
                        id = entry['id'],
                        home_team = entry['team_h'],
                        away_team = entry['team_a'],
                        home_team_goals = entry['stats'][1]["h"],
                        away_team_goals = entry['stats'][1]['a'],
                        home_team_assists = entry['stats'][2]['h'],
                        away_team_assists = entry['stats'][2]['a'],
                        home_team_own_goals = entry['stats'][3]['h'],
                        away_team_own_goals = entry['stats'][3]['a'],
                        home_team_penalties_saved = entry['stats'][4]['a'],
                        away_team_penalties_saved = entry['stats'][4]['h'],
                        home_team_penalties_missed = entry['stats'][5]['h'],
                        away_team_penalties_missed = entry['stats'][5]['a'],
                        home_team_yellow_cards = entry['stats'][6]['a'],
                        away_team_yellow_cards = entry['stats'][6]['h'],
                        home_team_red_cards = entry['stats'][7]['h'],
                        away_team_red_cards = entry['stats'][7]['a'],
                        home_team_saves = entry['stats'][8]['h'],
                        away_team_saves = entry['stats'][8]['a'],
                        )
                    match.save()
                    messages.info(request,"Added the gameweek")
            if pk == 0:
                if Match.objects.filter(id=entry['id']).exists:
                    pass
                else:
                    match = Match(
                        gameweek = entry['event'],
                        id = entry['id'],
                        home_team = entry['team_h'],
                        away_team = entry['team_a'],
                        home_team_goals = entry['stats'][1]["h"],
                        away_team_goals = entry['stats'][1]['a'],
                        home_team_assists = entry['stats'][2]['h'],
                        away_team_assists = entry['stats'][2]['a'],
                        home_team_own_goals = entry['stats'][3]['h'],
                        away_team_own_goals = entry['stats'][3]['a'],
                        home_team_penalties_saved = entry['stats'][4]['a'],
                        away_team_penalties_saved = entry['stats'][4]['h'],
                        home_team_penalties_missed = entry['stats'][5]['h'],
                        away_team_penalties_missed = entry['stats'][5]['a'],
                        home_team_yellow_cards = entry['stats'][6]['a'],
                        away_team_yellow_cards = entry['stats'][6]['h'],
                        home_team_red_cards = entry['stats'][7]['h'],
                        away_team_red_cards = entry['stats'][7]['a'],
                        home_team_saves = entry['stats'][8]['h'],
                        away_team_saves = entry['stats'][8]['a'],
                        )
                    match.save()
            
        return render(request,'add_match.html')

class MatchAPI(generics.ListAPIView):
    serializer_class = MatchSerializer
    def get_queryset(self):
        if 'home_team' in self.kwargs and 'away_team'in self.kwargs:
            return Match.objects.get(home_team=self.kwargs['home_team'],away_team=self.kwargs['away_team'])
        if 'id' in self.kwargs:
            return Match.objects.get(id=self.kwargs['id'])
        if 'gameweek' in self.kwargs:
            return Match.objects.filter(gameweek=self.kwargs['gameweek'])
        return Match.objects.all()
