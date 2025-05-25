from django.db import models
from django.contrib.auth.models import User


class CurrentBalance(models.Model):
      current_balance = models.FloatField(default=0)
      
      def __str__(self):
           return f"{self.current_balance}"
      
      
class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.CharField(max_length=200)
    expence_type = models.CharField(choices=(('CREDIT', 'CREDIT'), ('DEBIT', 'DEBIT')), max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.expence_type}: {self.description} - ${self.amount}"

class RequestLogs(models.Model):
      request_info = models.TextField()
      request_type = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add=True)