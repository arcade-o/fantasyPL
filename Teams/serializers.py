from .models import Player,Teams,TransferMarket,Transfer
from rest_framework import serializers

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ("id", "first_name","last_name","team_id","fee")

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ("Name","id")

class TransferMarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferMarket
        fields = ("id","seller_id","player_id","fee")

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ("id","seller_id","player_id","fee","buyer_id")
        
        