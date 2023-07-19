from django.contrib import admin
from .models import Voting, Vote, Character
from django.db import models

admin.site.register(Character)


class ParticipantVotingInlineForVoting(admin.TabularInline):
    model = Vote
    extra = 3


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    inlines = [ParticipantVotingInlineForVoting]
