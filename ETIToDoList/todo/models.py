from django.db import models
from datetime import datetime

class TodoItem(models.Model):
    content = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    deleted = models.BooleanField(default=False)
    userID = models.IntegerField(default=1)
