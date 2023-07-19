from rest_framework import serializers
from .models import Voting, Character


class VotingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = ('id', 'title',)


class VotingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = '__all__'


class VotingCharactersSerializer(serializers.ModelSerializer):
    characters = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Voting
        fields = ('characters',)
