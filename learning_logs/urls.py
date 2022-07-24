"""Defines URL patterns for learning_logs."""
from django.urls import path, include
from . import views


app_name = "learning_logs"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
    # Detail for a single topic.
    path("topics/<int:topic_id>/", views.topic, name="topic"),
]
