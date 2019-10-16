from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *


# Create your views here.

from . models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'batman'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    form_class = addBlog

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    form_class = editBlog

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    context_object_name = 'batman'
    success_url = reverse_lazy('home')
