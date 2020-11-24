from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import *
from .forms  import *
from recommender.recommend import *
from .utils import *

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
    queryset = list(Book.objects.all())
    context_object_name = 'books'
    paginate_by = 20

class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recommender = ContentBasedBookRecommender()
        print(self.kwargs['pk'])
        context['book'] = Book.objects.get(id=self.kwargs['pk'])
        titles = recommender.recommend(item_id=self.kwargs['pk'], num=10)
        rec_books = modelize(list(titles))
        context['to_recommend'] = list(rec_books)
        print(recommender.recommend(item_id=self.kwargs['pk'], num=10))
        return context
