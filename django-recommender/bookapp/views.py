from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from .models import *
from .forms  import *

def home(request):
    return HttpResponse('<h1 style="color:green;">Hello, Sailor</h1>')

class UserCreateView(SuccessMessageMixin,CreateView):
    template_name   = 'signup.html'
    success_url     = '/books/'
    form_class      = UserRegistrationForm
    success_message = "Author has been successfully registered!"

class BookCreateView(SuccessMessageMixin,CreateView):
    template_name   = 'book_create.html'
    form_class      =  BookCreationForm
    success_message =  "Book has been successfully created"
    success_url     =  '/books/'

class BookView(ListView):
    template_name = 'book_list.html'
    queryset      = Book.objects.all()
    context_object_name = 'books'

class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book
