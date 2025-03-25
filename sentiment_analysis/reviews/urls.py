from django.urls import path
from .views import analyze_review

urlpatterns = [
    path('analyze/', analyze_review, name='analyze_review'),
]
