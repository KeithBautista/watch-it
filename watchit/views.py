from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import DeleteView
"""List View does a query set and provides all views of a specific post while
the detail view shows the specific details of a post"""
from .models import Post, Category, Comment
from .forms import PostForm, UpdatePost
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
"""We need to import Post from the models in able to use it"""
"""We also need to import PostForm from forms.py to use it"""


# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    # Checks if a user has liked a post

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('movie-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    """This view will show all the posts since we passed in
    listview"""
    category = Category.objects.all()
    ordering = ['-id']
    # place in -post_date to show most recent post

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


def CategoryView(request, category):
    category_posts = Post.objects.filter(category=category)
    context = {}
    context['category_posts'] = category_posts
    category_menu = Category.objects.all()
    context["category_menu"] = category_menu
    return render(request, 'categories.html', context)


class MovieDetailView(DetailView):
    model = Post
    template_name = 'movie_details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(MovieDetailView, self).get_context_data(*args, **kwargs)
        getid = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = getid.total_likes()

        liked = False
        if getid.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["category_menu"] = category_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddMovieView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'movie_add.html'
    # fields = '__all__' // Commented out since PostForms was created
    """If you dont want to include all fields,
    you can just create a python list like
    fields = ('title', 'body') """

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(AddMovieView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = '__all__' 


class UpdateMovieView(UpdateView):
    model = Post
    form_class = UpdatePost
    template_name = 'movie_update.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(UpdateMovieView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


class DeleteMovieView(DeleteView):
    model = Post
    template_name = 'movie_delete.html'
    fields = ['title',  'title_tag', 'body']
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(DeleteMovieView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


def index(request):
    return render(request, 'movie-details.html')