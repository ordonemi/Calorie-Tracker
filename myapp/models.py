from django.db import models
from django.utils import timezone

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_entered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Entries"