from django.urls import path
from .views import ArticleListView, ArticleEditView, ArticleDetailView, ArticleDeleteView, ArticleCreateView

urlpatterns=[
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit', ArticleEditView.as_view(), name='article_edit'),
    path('create', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
]