from rest_framework import serializers
from ..team.models import Portfolio,Team


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Portfolio
        frields='__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        frields="__all__"
