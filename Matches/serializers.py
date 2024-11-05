from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model: Match
        fields = ("gameweek","home_team","away_team","home_team_goals","home_team_assists","home_team_own_goals",
                  "home_team_penalties_saved","home_team_penalties_missed",
                  "home_team_yellow_cards", "home_team_red_cards","home_team_saves",
                  "away_team_goals","away_team_assists","away_team_own_goals","away_team_penalties_saved","away_team_penalties_missed",
                  "away_team_yellow_cards","away_teams_red_cards","away_team_saves")