from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Purchase
from .serializers import PurchaseSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
