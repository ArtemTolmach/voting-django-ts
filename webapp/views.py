from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Voting, Vote
from .serializers import VotingListSerializer, VotingDetailSerializer, VotingCharactersSerializer


class VotingListView(APIView):
    """Вывод списка голосований"""

    def get(self, request):
        voting = Voting.objects.all()
        serializer = VotingListSerializer(voting, many=True)

        for vote in serializer.data:
            voting_obj = Voting.objects.get(id=vote['id'])
            vote['is_active'] = voting_obj.is_active()

        return Response(serializer.data)


class VotingDetailView(APIView):
    """Вывод списка голосований"""

    def get(self, request, pk):
        voting = Voting.objects.get(id=pk)
        serializer = VotingDetailSerializer(voting)
        return Response(serializer.data)


class VotingCharactersView(APIView):
    """Вывод списка участников"""

    def get(self, request, pk):
        voting = Voting.objects.get(id=pk)
        serializer = VotingCharactersSerializer(voting)
        return Response(serializer.data)


class UpCharacterVoice(APIView):
    """Увеличение голосов"""

    def post(self, request, id_voting, id_character):
        try:
            part = Vote.objects.get(voting=id_voting, character=id_character)
            part.voices += 1
            part.save()
            return Response("OK")
        except:
            return Response("NOT OK")


class ListWinners(APIView):
    """Список победителей"""

    def get(self, request):
        list_winners = Vote.objects.filter(is_winner=True)
        return Response(list(list_winners.values()))
