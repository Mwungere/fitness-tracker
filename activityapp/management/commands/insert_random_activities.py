from django.core.management.base import BaseCommand
from random import choice, randint
from datetime import timedelta, date
from activityapp.models import Activity
from userapp.models import User

class Command(BaseCommand):
    help = 'Insert random activities for a user'

    def handle(self, *args, **kwargs):
        user = User.objects.first()  # You can adjust this to fetch a specific user
        if user:
            activity_types = ['sport', 'sleep', 'work', 'leisure']
            activity_names = [
                'Running', 'Swimming', 'Cycling', 'Yoga', 'Reading', 'Sleeping', 'Jogging', 
                'Meditation', 'Cooking', 'Walking', 'Working on project', 'Watching TV', 'Guitar practice'
            ]
            activities = []
            for _ in range(500):
                name = choice(activity_names)
                duration = timedelta(hours=randint(1, 3), minutes=randint(0, 59), seconds=randint(0, 59))
                date_activity = date(randint(2020, 2024), randint(1, 12), randint(1, 28))
                activity_type = choice(activity_types)

                activity = Activity(
                    user=user,
                    name=name,
                    duration=duration,
                    date=date_activity,
                    activity_type=activity_type
                )
                activities.append(activity)

            Activity.objects.bulk_create(activities)
            self.stdout.write(self.style.SUCCESS(f"500 random activities inserted for user {user.username} successfully."))
        else:
            self.stdout.write(self.style.ERROR("No user found. Please ensure you have a valid user."))
