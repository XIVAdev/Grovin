from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PortfolioSerializer,TeamSerializer
from team.models import Portfolio,Team
from rest_framework.viewsets import ModelViewSet


class PortfolioViewSet(ModelViewSet):
    queryset=Portfolio.objects.all()
    serializer_class=PortfolioSerializer


class TeamViewSet(ModelViewSet):
    queryset=Team.objects.all()
    serializer_class=TeamSerializer







