from django.shortcuts import render
from django.views.generic import ListView, DetailView
"""List View does a query set and provides all views of a specific post while
the detail view shows the specific details of a post"""

# Create your views here.


# def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    """This view will show all the posts since we passed in
    listview"""
