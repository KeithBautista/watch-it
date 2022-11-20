from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
"""List View does a query set and provides all views of a specific post while
the detail view shows the specific details of a post"""
from .models import Post
from .forms import PostForm
"""We need to import Post from the models in able to use it"""
"""We also need to import PostForm from forms.py to use it"""


# Create your views here.


# def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    """This view will show all the posts since we passed in
    listview"""


class MovieDetailView(DetailView):
    model = Post
    template_name = 'movie_details.html'


class AddMovieView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'movie_add.html'
    # fields = '__all__' // Commented out since PostForms was created
    """If you dont want to include all fields,
    you can just create a python list like
    fields = ('title', 'body') """


class UpdateMovieView(UpdateView):
    model = Post
    template_name = 'movie_update.html'
    fields = ['title',  'title_tag', 'body']
    