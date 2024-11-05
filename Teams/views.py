from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
import urllib,json
from .models import Player,GK,DEF,MID,FWRD,Teams,Transfer,TransferMarket
from rest_framework import generics
from .serializers import TeamsSerializer,PlayerSerializer,TransferSerializer,TransferMarketSerializer
from rest_framework.response import Response
# Create your views here.

class add_players(UserPassesTestMixin,View):
    def test_func(self):
        return self.request.user.is_superuser
    
    def get(self,request):
        url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
        data = json.loads(urllib.request.urlopen(url).read())
        for entry in data['elements']:
            if entry['element_type'] == 1:
                player = GK(id = entry['id'],
                            first_name = entry['first_name'],
                            last_name = entry['second_name'],
                            team_id = entry['team'],
                            )
                player.save()
            if entry['element_type'] == 2:
                player = DEF(id = entry['id'],
                            first_name = entry['first_name'],
                            last_name = entry['second_name'],
                            team_id = entry['team'],
                            )
                player.save()
            if entry['element_type'] == 3:
                player = MID(id = entry['id'],
                            first_name = entry['first_name'],
                            last_name = entry['second_name'],
                            team_id = entry['team'],
                            )
                player.save()
            if entry['element_type'] == 4:
                player = GK(id = entry['id'],
                            first_name = entry['first_name'],
                            last_name = entry['second_name'],
                            team_id = entry['team'],
                            )
                player.save()
        return render(request,'add_players.html')
    
class add_teams(UserPassesTestMixin,View):
    def test_func(self):
        return self.request.user.is_superuser
    
    def get(self,request):
        url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
        data = json.loads(urllib.request.urlopen(url).read())
        for entry in data['teams']:
            team = Teams(
                id = entry['id'],
                Name = entry['name'],
            )
            team.save()
        return render(request,'add_teams.html')
    
class TeamsAPI(generics.ListAPIView):
    serializer_class = TeamsSerializer
    def get_queryset(self):
        if 'id' in self.kwargs:
            return Teams.objects.get(id=self.kwargs['id'])
        return Teams.objects.all()
    
class PlayersAPI(generics.ListAPIView):
    serializer_class = PlayerSerializer
    def get_queryset(self):
        if 'pos' in self.kwargs:
            if self.kwargs['pos'] == 1:
                return GK.objects.all()
            if self.kwargs['pos'] == 2:
                return DEF.objects.all()
            if self.kwargs['[pos'] == 3:
                return MID.objects.all()
            if self.kwargs['pos'] == 4:
                return FWRD.objects.all()
        if 'id' in self.kwargs:
            return Player.objects.get(id=self.kwargs['id'])
        if 'team' in self.kwargs:
            return Player.objects.get(team_id=self.kwargs['team'])
        return Player.objects.all()
    
class TransfersAPI(generics.ListAPIView,generics.CreateAPIView):
    serializer_class = TransferSerializer
    def get_queryset(self):
        if 'seller_id' in self.kwargs:
            return Transfer.objects.filter(seller_id = self.kwargs['seller_id'])
        if 'player_id' in self.kwargs:
            return Transfer.objects.filter(player_id = self.kwargs['player_id'])
        if 'buyer_id' in self.kwargs:
            return Transfer.objects.filter(buyer_id = self.kwargs['buyer_id'])
        if 'id' in self.kwargs:
            return Transfer.objects.get(id=self.kwargs['id'])
        return Transfer.objects.all()
    
    def get_object(self):
        return Transfer.objects.get(id=self.kwargs['id'])
    
    def post(request,self,*args,**kwargs):
        serializer = serializer(request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)

class TransferMarketAPI(generics.ListAPIView,generics.CreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    serializer_class = TransferMarketSerializer
    def get_object(self):
        return TransferMarket.objects.get(id=self.kwargs['id'])
    
    def get_queryset(self):
        if 'id' in self.kwargs:
            return TransferMarket.objects.get(id=self.kwargs['id'])
        if 'seller_id' in self.kwargs:
            return TransferMarket.objects.filter(seller_id=self.kwargs['seller_id'])
        if 'player_id' in self.kwargs:
            return TransferMarket.objects.filter(seller_id = self.kwargs['player_id'])
        return TransferMarket.objects.all()
    
    def post(request,self,*args,**kwargs):
        serializer = serializer(request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    
    def put(request,self,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(request,self,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)