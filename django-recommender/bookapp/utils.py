from .models import *
from typing import Iterable


def modelize(obj):
    if isinstance(obj, Iterable):
        for o in obj:
            book = Book.objects.get(id=o)
            yield book
    else:
        return Book.objects.get(title=obj)
