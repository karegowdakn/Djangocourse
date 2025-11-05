from django.urls import path
from app.views import ArticleDeleteView, ArticleCreateView, ArticleListView, ArticleUpdateView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('create/', ArticleCreateView.as_view(), name='create_article'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update_article'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete_article'),
]
