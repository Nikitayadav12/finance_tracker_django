from django.urls import path
from .views import FinanceEntryListCreateView, FinanceEntryDetailView

urlpatterns = [
    path('entries/', FinanceEntryListCreateView.as_view()),
    path('entries/<int:pk>/', FinanceEntryDetailView.as_view()),
]