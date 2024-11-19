import pandas as pd # type: ignore
from django.core.management.base import BaseCommand
from activityapp.models import Activity, Recommendation


# Step 2: Fetch data from the database
def fetch_data():
    """
    Fetch data from the Activity and Recommendation models.
    Convert the QuerySets to pandas DataFrames.
    """
    activities = Activity.objects.all().values(
        'id',
        'user__username',  # Fetch username
        'name',
        'duration',
        'date',
        'activity_type'
    )
    recommendations = Recommendation.objects.all().values(
        'activity_id',
        'text'
    )

    activities_df = pd.DataFrame(list(Activity.objects.values('id', 'name', 'duration', 'date', 'activity_type')))
    recommendations_df = pd.DataFrame(list(Recommendation.objects.values('id', 'activity_id', 'text')))
    print("Activities DataFrame columns:", activities_df.columns)
    print("Recommendations DataFrame columns:", recommendations_df.columns)

    return activities_df, recommendations_df


# Step 3: Perform operations on DataFrames
def analyze_data(activities_df, recommendations_df):
    # Debug: Check DataFrame structures
    print("Activities DataFrame columns:", activities_df.columns)
    print("Recommendations DataFrame columns:", recommendations_df.columns)
    print("Number of recommendations:", len(recommendations_df))

    # Check if recommendations_df is empty
    if recommendations_df.empty:
        print("No recommendations data found. Skipping merge.")
        return activities_df, pd.DataFrame(), pd.Series()

    # Perform the merge
    merged_df = activities_df.merge(
        recommendations_df, left_on='id', right_on='activity_id', how='left'
    )

    # Analyze specific activity types
    sport_activities = merged_df[merged_df['activity_type'] == 'sport']
    duration_summary = merged_df.groupby('activity_type')['duration'].sum()

    return merged_df, sport_activities, duration_summary


# Step 4: Save DataFrame to CSV
def save_to_file(df, filename):
    """
    Save a pandas DataFrame to a CSV file.
    """
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


class Command(BaseCommand):
    """
    Django management command to extract and analyze activities data.
    """
    help = 'Extract all activities and their recommendations into a DataFrame'

    def handle(self, *args, **kwargs):
        # Step 1: Fetch data
        self.stdout.write("Fetching data from the database...")
        activities_df, recommendations_df = fetch_data()

        if activities_df.empty:
            self.stdout.write(self.style.WARNING("No activity data found."))
            return

        # Step 2: Analyze data
        self.stdout.write("Analyzing data...")
        merged_df, sport_activities, duration_summary = analyze_data(activities_df, recommendations_df)

        # Step 3: Save results to files
        self.stdout.write("Saving results to files...")
        save_to_file(merged_df, "merged_activities.csv")
        save_to_file(sport_activities, "sport_activities.csv")

        # Save the duration summary to CSV
        duration_summary.to_csv("duration_summary.csv", header=True)
        self.stdout.write("Files saved successfully!")

        # Step 4: Display summaries in the console
        self.stdout.write(self.style.SUCCESS("\nMerged Activities:"))
        self.stdout.write(str(merged_df.head()))

        self.stdout.write(self.style.SUCCESS("\nSport Activities:"))
        self.stdout.write(str(sport_activities.head()))

        self.stdout.write(self.style.SUCCESS("\nDuration Summary:"))
        self.stdout.write(str(duration_summary))

        self.stdout.write(self.style.SUCCESS("Data extraction and analysis completed successfully!"))
