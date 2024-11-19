from django.urls import path
from .views import activity_list, activity_add, activity_edit, activity_delete

urlpatterns = [
    path( ' ' , activity_list, name="activity_list" ),
    path('add/', activity_add, name='activity_add'),
    path('edit/<int:activity_id>/', activity_edit, name='activity_edit'),
    path('delete/<int:pk>/', activity_delete, name='activity_delete'),
]
