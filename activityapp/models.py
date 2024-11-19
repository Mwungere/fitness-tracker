from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from datetime import timedelta

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.DurationField()
    date = models.DateField()
    activity_type = models.CharField(
        max_length=50,
        choices=[
            ('sport', 'Sport'),
            ('sleep', 'Sleep'),
            ('work', 'Work'),
            ('leisure', 'Leisure'),
        ],
        default='leisure'
    )

    def __str__(self):
        return f"{self.name} ({self.activity_type})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the original save method
        generate_recommendations(self)


@receiver(post_delete, sender=Activity)
def delete_recommendations(sender, instance, **kwargs):
    if hasattr(instance, 'recommendations'):
        instance.recommendations.all().delete()


def generate_recommendations(instance):
    # Example recommendation logic
    if instance.activity_type == 'sleep':
        if instance.duration < timedelta(hours=7):
            Recommendation.objects.update_or_create(
                activity=instance,
                text='Try to sleep at least 7 hours for better health.'
            )
    elif instance.activity_type == 'sport':
        if instance.duration < timedelta(hours=1):
            Recommendation.objects.update_or_create(
                activity=instance,
                text='Aim for at least 1 hour of exercise daily.'
            )


class Recommendation(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='recommendations')
    text = models.TextField()

    def __str__(self):
        return self.text
