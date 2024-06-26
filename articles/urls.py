from django.urls import path
from .views import (
    ArticleListView, ArticleDetailView, ArticleCreateView,
    ArticleUpdateView, ArticleDeleteView
)

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/create/', ArticleCreateView.as_view(), name='article-create'),
    path('article/update/<int:pk>/', ArticleUpdateView.as_view(), name='article-update'),
    path('article/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article-delete'),
]