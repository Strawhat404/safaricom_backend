from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Bank, Branch, Application
from .serializers import BankSerializer, BranchSerializer, ApplicationSerializer

# GET /api/banks
class BankListView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

# GET /api/branches?bank_id={id}
class BranchListView(generics.ListAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        bank_id = self.request.query_params.get('bank_id', None)
        if bank_id is not None:
            return Branch.objects.filter(bank_id=bank_id)
        return Branch.objects.none()  # Return empty if no bank_id

# POST /api/applications/submit
class ApplicationSubmitView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)