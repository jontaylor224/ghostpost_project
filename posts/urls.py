from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('api/posts/<int:pk>/post_detail.html',
         views.post_detail, name='post_detail'),
    path('api/posts/<str:post_id>', views.delete_post, name='delete_post'),
    path('api/posts/upvote/<int:pk>', views.upvote, name='upvote'),
    path('api/posts/downvote/<int:pk>', views.downvote, name='downvote'),
]
