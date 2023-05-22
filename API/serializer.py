from rest_framework import serializers
from team.models import Portfolio,Team


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Portfolio
        fields='__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields="__all__"
