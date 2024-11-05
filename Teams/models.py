from django.db import models
from datetime import datetime

# Create your models here.

class Teams(models.Model):
    Name = models.TextField(max_length = 50)

    def __str__(self):
        return self.Name

class Player(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    team_id = models.IntegerField()
    fee = 10000

    def __str__(self):
        return str(self.id)
    

class GK(Player):
    save_mx = 3
    cleansheet_mx = 3
    assist_mx = 5
    goal_mx = 10

class DEF(Player):
    cleansheet_mx = 3
    assist_mx = 3
    goal_mx = 5

class MID(Player):
    cleansheet_mx = 2
    assist_mx = 2
    goal_mx = 4

class FWRD(Player):
    assist_mx = 2
    goal_mx = 2

class TransferMarket(models.Model):
    seller_id = models.IntegerField()
    fee = models.IntegerField()
    player_id = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Transfer(models.Model):
    seller_id = models.IntegerField()
    fee = models.IntegerField()
    player_id = models.IntegerField()
    buyer_id = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.id)