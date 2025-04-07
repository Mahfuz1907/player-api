from rest_framework import serializers
from .models import Player, Category, Team, Head


class HeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Head
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source = 'category.name')

    class Meta:
        model = Player
        fields = '__all__'
