from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Result, Team

@receiver(post_save, sender=Result)
def update_team_score(sender, instance, created, **kwargs):
    if created:
        # Get the team from the student's team
        team = instance.student.team
        
        # Add the score from the result to the team's points
        team.points += instance.score
        
        # Save the updated team instance
        team.save()
