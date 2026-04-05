from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import calculate_financial_summary, category_breakdown
from users.permissions import IsAnalystOrAdmin


class SummaryView(APIView):
    permission_classes = []

    def get(self, request):
        user = request.user
        data = calculate_financial_summary(user)
        return Response(data)


class CategoryView(APIView):
    permission_classes = [IsAuthenticated, IsAnalystOrAdmin]

    def get(self, request):
        user = request.user
        data = category_breakdown(user)
        return Response(data)