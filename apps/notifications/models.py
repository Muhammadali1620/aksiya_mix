from django.db import models

from apps.companies.models import Company


class Notification(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=50)
    message = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title