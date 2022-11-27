"""watch_it URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import HomeView
from .views import MovieDetailView
from .views import AddMovieView
from .views import UpdateMovieView
from .views import DeleteMovieView
from .views import CategoryView
from .views import LikeView
from .views import AddCommentView

urlpatterns = [
    # path('', views.home, name="home"),
    # Since we are using class based views we need to change this to the below
    path('', HomeView.as_view(), name="home"),
    path('movie/<int:pk>', MovieDetailView.as_view(), name="movie-detail"),
    path('add_movie/', AddMovieView.as_view(), name="add-movie"),
    path('movie/edit/<int:pk>', UpdateMovieView.as_view(), name="edit-movie"),
    path('movie/delete/<int:pk>', DeleteMovieView.as_view(), name="delete-movie"),
    path('category/<str:category>/', CategoryView, name="category"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('movie/<int:pk>/comment/', AddCommentView, name="add-comment"),
]
