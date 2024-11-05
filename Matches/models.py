from django.db import models

# Create your models here.

class Match(models.Model):
    gameweek = models.IntegerField()
    home_team = models.IntegerField()
    away_team = models.IntegerField()
    home_team_goals = models.JSONField()
    home_team_assists = models.JSONField()
    home_team_own_goals = models.JSONField()
    home_team_penalties_saved = models.JSONField()
    home_team_penalties_missed = models.JSONField()
    home_team_yellow_cards = models.JSONField()
    home_team_red_cards = models.JSONField()
    home_team_saves = models.JSONField()
    away_team_goals = models.JSONField()
    away_team_assists = models.JSONField()
    away_team_own_goals = models.JSONField()
    away_team_penalties_saved = models.JSONField()
    away_team_penalties_missed = models.JSONField()
    away_team_yellow_cards = models.JSONField()
    away_team_red_cards = models.JSONField()
    away_team_saves = models.JSONField()

    def __str__(self):
        return str(self.id)

