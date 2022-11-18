from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
"""List View does a query set and provides all views of a specific post while
the detail view shows the specific details of a post"""
from .models import Post
"""We need to import Post from the models in able to use it"""

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
    template_name = 'movie_add.html'
    fields = '__all__'
    """If you dont want to include all fields,
    you can just create a python list like
    fields = ('title', 'body') """
