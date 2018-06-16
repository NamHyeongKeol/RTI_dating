from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='cards')
    partner = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='exposed_cards')
    is_deleted = models.BooleanField(db_index=True, default=False, null=False)
    is_seen = models.BooleanField(db_index=True, default=False, null=False)
