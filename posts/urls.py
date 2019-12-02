from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path(
        'boasts_only/',
        views.time_sorted_only_boasts_view,
        name='boasts_only'),
    path('roasts_only/',
         views.time_sorted_only_roasts_view,
         name='roasts_only'),
    path('votes_all/', views.votes_sorted_index, name='votes_all'),
    path('votes_boasts_only', views.vote_sorted_only_boasts_view,
         name='votes_boasts_only'),
    path('votes_roasts_only', views.vote_sorted_only_roasts_view,
         name='votes_roasts_only'),
    path('api/posts/<int:pk>/post_detail.html',
         views.post_detail, name='post_detail'),
    path('api/posts/<str:post_id>', views.delete_post, name='delete_post'),
    path('api/posts/upvote/<int:pk>', views.upvote, name='upvote'),
    path('api/posts/downvote/<int:pk>', views.downvote, name='downvote'),
]
