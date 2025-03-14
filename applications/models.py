from django.db import models

class Bank(models.Model):
    value = models.CharField(max_length=255)  # Bank name

    def __str__(self):
        return self.value

class Branch(models.Model):
    value = models.CharField(max_length=255)  # Branch name
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)  # Foreign key to Bank

    def __str__(self):
        return self.value

class Application(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Submitted', 'Submitted'),
    )

    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    proof_file = models.FileField(upload_to='proofs/', null=True, blank=True)  # For file upload

    def __str__(self):
        return f"{self.account_name} - {self.account_number}"