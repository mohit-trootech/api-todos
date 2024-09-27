from django.db.models import *
from django_extensions.db.models import TitleDescriptionModel, TimeStampedModel


class Todo(TitleDescriptionModel, TimeStampedModel):

    def __str__(self):
        return self.title
