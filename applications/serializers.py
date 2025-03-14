from rest_framework import serializers
from .models import Bank, Branch, Application

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'value']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'value']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'bank_name', 'branch_name', 'account_name', 'account_number', 'status', 'proof_file', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']