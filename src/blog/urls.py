from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]