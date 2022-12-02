from django.db import models
import uuid


class reportModel(models.Model):
    TYPE_CHOICES = (
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly')
    )
    reportId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    typeReport = models.CharField(max_length=1,choices=TYPE_CHOICES)
    
    class Meta:
        db_table = 'report'
    