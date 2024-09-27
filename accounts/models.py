from django.contrib.auth.models import AbstractUser
from django.db.models import UUIDField
from uuid import uuid4
from django_extensions.db.fields import CreationDateTimeField


class User(AbstractUser):
    api_key = UUIDField(unique=True, editable=False, default=uuid4())
    api_created = CreationDateTimeField(editable=True)

    def __str__(self):
        return self.username
