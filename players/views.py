from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Player, Category, Team, Head
from .serializers import PlayerSerializer, CategorySerializer, TeamSerializer, HeadSerializer



class Heads(APIView):
    def get(self, request):
        heads = Head.objects.all()
        serializer = HeadSerializer(heads, many=True)
        return Response(serializer.data)
        

class HeadById(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            head = Head.objects.get(id = id)
            serializer = HeadSerializer(head)
            return Response(serializer.data)
        except Head.DoesNotExist:
            return Response({'error': 'Not found anything'}, status=404)
        


class Teams(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


class TeamDetail(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            team = Team.objects.get(id=id) 
            serializer = TeamSerializer(team) 
            return Response(serializer.data)  
        except Team.DoesNotExist:
            return Response({'error': 'Team not found'}, status=404)



class Categories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
        
class PlayerList(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

class PlayerSearch(APIView):
    def get(self, request):
        players = Player.objects.all()

        search_query = request.GET.get('search', None)  
        role_filter = request.GET.get('role', None)  
        country_filter = request.GET.get('country', None)  
        category_filter = request.GET.get('category', None)

        if search_query:
            players = players.filter(name__icontains=search_query) | players.filter(short_name__icontains=search_query)

        if role_filter:
            players = players.filter(role=role_filter)

        if country_filter:
            players = players.filter(country=country_filter)

        if category_filter:
            players = players.filter(category=category_filter)


        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    

class PlayerByCategory(APIView):
    def get(self, request, id):
        players = Player.objects.filter(category_id = id)
        

        if not players.exists():
            return Response({'error': 'No players found for this category'}, status=404)
        
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    

class PlayerByTeam(APIView):
    def get(self, request, id):
        players = Player.objects.filter(team_id = id)

        if not players.exists():
            return Response({'error': 'No players found for this team'}, status=404)
        
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    
    def post(self, request, id):
        try:
            team = Team.objects.get(id = id)
        except Team.DoesNotExist:
            return Response({'error': 'Team not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            player_id = request.data.get('id')  
            player = Player.objects.get(id=player_id)
        except Player.DoesNotExist:
            return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)

        
        player.team = team
        player.save()


        serializer = PlayerSerializer(player)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

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
        

class PlayersByCountry(APIView):
    def get(self, request, country, *args, **kwargs): 
            players = Player.objects.filter(country=country)
            if players.exists():
                serializer = PlayerSerializer(players, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'No players found for the given country name'}, status=404)
            

class PlayerByRole(APIView):
    def get(self, request, role, *args, **kwargs):
        players = Player.objects.filter(role=role)
        if players.exists():
            serializer = PlayerSerializer(players, many=True)
            return Response(serializer.data)
        else: 
            return Response({'error': 'No players found for the given role'}, status=404)
        


class PlayerByCountryRole(APIView):
    def get(self, requset, country, role, *args, **kwargs):
        players = Player.objects.filter(country=country, role=role)
        if players.exists():
            serializer = PlayerSerializer(players, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'No players found for the given team and role'}, status=404)
        



        