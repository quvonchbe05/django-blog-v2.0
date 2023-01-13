from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy

# Create your views here.

class ArticleListView(ListView):
    model=Article
    template_name='pages/article_list.html'

class ArticleCreateView(CreateView):
    model=Article
    fields=['title','summary','body','photo','author']
    template_name='pages/article_create.html'

class ArticleDetailView(DeleteView):
    model=Article
    template_name='pages/article_detail.html'

class ArticleEditView(UpdateView):
    model=Article
    fields=['title','summary','body','photo']
    template_name='pages/article_edit.html'

class ArticleDeleteView(DeleteView):
    model=Article
    template_name='pages/article_delete.html'
    success_url=reverse_lazy('article_list')