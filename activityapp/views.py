from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity
from django.core.paginator import Paginator
from .forms import  ActivityForm


def activity_list(request):
    activities = Activity.objects.filter(user=request.user)
    paginator = Paginator(activities, 20)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    recommendations = generate_recommendations(activities)

    return render(request, 'activityapp/activity_list.html', {
        'page_obj': page_obj,
        'recommendations': recommendations,
    })


def generate_recommendations(activities):
    recommendations = []
    total_sleep = sum(activity.duration.total_seconds() for activity in activities if activity.activity_type == 'sleep')
    total_sport = sum(activity.duration.total_seconds() for activity in activities if activity.activity_type == 'sport')


    # assume recommendations
    if total_sleep < 8 * 3600:  # Less than 8 hours of sleep
        recommendations.append("Consider increasing your sleep duration for better health.")
    if total_sport < 150 * 60:  # Less than 150 minutes of sport per week
        recommendations.append("Try to incorporate more physical activities into your routine.")

    return recommendations

def activity_add(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            print("Reached here")
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            return redirect('activity_list')
    else:
        form = ActivityForm()
    return render(request, 'activityapp/activity_form.html', {'form': form})

def activity_edit(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id, user=request.user)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'activityapp/activity_form.html', {'form': form})
def activity_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk, user=request.user)
    if request.method == "POST":
        activity.delete()
        return redirect('activity_list')
    return render(request, 'activityapp/activity_confirm_delete.html', {'activity': activity})
