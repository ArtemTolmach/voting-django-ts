from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Voting, Vote
from django.utils import timezone


@receiver(post_save, sender=Vote)
def check_votes(sender, instance, **kwargs):
    max_voices = Voting.objects.get(id=instance.voting.id).max_voices
    if instance.voices >= max_voices:
        Vote.objects.filter(id=instance.id).update(is_winner=True)
        Voting.objects.filter(id=instance.voting).update(is_active=False)
