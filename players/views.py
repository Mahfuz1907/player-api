from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Player
from .serializers import PlayerSerializer

class PlayerList(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


class PlayerDetail(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            player = Player.objects.get(id=id)  # Fetch player by ID
            serializer = PlayerSerializer(player)  # Serialize the specific player
            return Response(serializer.data)  # Send serialized data as response
        except Player.DoesNotExist:
            return Response({'error': 'Player not found'}, status=404)
        

class PlayerByShortName(APIView):
    def get(self, request, short_name, *args, **kwargs):
        try:
            player = Player.objects.get(short_name=short_name)  # Query by short_name
            serializer = PlayerSerializer(player)
            return Response(serializer.data)  # Return the serialized player data
        except Player.DoesNotExist:
            return Response({'error': 'Player not found'}, status=404)
        

class PlayersByTeam(APIView):
    def get(self, request, team, *args, **kwargs): 
            players = Player.objects.filter(team=team)
            if players.exists():
                serializer = PlayerSerializer(players, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'No players found for the given team name'}, status=404)
            

class PlayerByRole(APIView):
    def get(self, request, role, *args, **kwargs):
        players = Player.objects.filter(role=role)
        if players.exists():
            serializer = PlayerSerializer(players, many=True)
            return Response(serializer.data)
        else: 
            return Response({'error': 'No players found for the given role'}, status=404)
        


class PlayerByTeamRole(APIView):
    def get(self, requset, team, role, *args, **kwargs):
        players = Player.objects.filter(team=team, role=role)
        if players.exists():
            serializer = PlayerSerializer(players, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'No players found for the given team and role'}, status=404)
        


class PlayerByCategory(APIView):
    def get(self, request, category, *args, **kwargs):
        players = Player.objects.filter(category=category)
        if players.exists():
            serializer = PlayerSerializer(players, many=True)
            return Response(serializer.data)
        else: 
            return Response({'error': 'No players found for the given category'})
        