from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import FinanceEntry
from .serializers import FinanceEntrySerializer
from users.permissions import IsAdmin


class FinanceEntryListCreateView(generics.ListCreateAPIView):
    serializer_class = FinanceEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FinanceEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FinanceEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FinanceEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FinanceEntry.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]