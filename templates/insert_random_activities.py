from random import choice, randint
from datetime import timedelta, date
from django.contrib.auth.models import User
from activityapp.models import Activity
import random

# Assume you have a user already logged in or passed (e.g., request.user in views)
# For shell, manually define the user to associate with activities
user = User.objects.first()  # Get the first user or any specific user

if user:  # Make sure the user exists
    # Define sample data for activity types
    activity_types = ['sport', 'sleep', 'work', 'leisure']
    activity_names = [
        'Running', 'Swimming', 'Cycling', 'Yoga', 'Reading', 'Sleeping', 'Jogging', 
        'Meditation', 'Cooking', 'Walking', 'Working on project', 'Watching TV', 'Guitar practice'
    ]
    
    # Generate random activities for the specific user
    activities = []
    for _ in range(500):
        name = choice(activity_names)  # Random activity name
        duration = timedelta(hours=randint(1, 3), minutes=randint(0, 59), seconds=randint(0, 59))  # Random duration
        date_activity = date(randint(2020, 2024), randint(1, 12), randint(1, 28))  # Random date
        activity_type = choice(activity_types)  # Random activity type

        # Create an Activity object with the user
        activity = Activity(
            user=user,
            name=name,
            duration=duration,
            date=date_activity,
            activity_type=activity_type
        )
        activities.append(activity)

    # Bulk insert activities into the database for the specific user
    Activity.objects.bulk_create(activities)

    print(f"500 random activities inserted for user {user.username} successfully.")
else:
    print("No user found. Please ensure you have a valid user.")
