

from django.urls import path
from .views import *

urlpatterns = [
    path('comment/<int:pk>/', CreateComment.as_view(), name='create_comment'),
    path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/', PostListView.as_view(), name='post_list'),
    path('', HomeView.as_view(), name='home'),
]