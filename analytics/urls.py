from django.urls import path
from .views import SummaryView, CategoryView

urlpatterns = [
    path('summary/', SummaryView.as_view()),
    path('categories/', CategoryView.as_view()),
]