from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('author_create/', UserCreateView.as_view(), name='author_create'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('all/', BookView.as_view(), name='all'),
    path('all/<int:pk>/', BookDetailView.as_view(), name='detailed_book'),
]