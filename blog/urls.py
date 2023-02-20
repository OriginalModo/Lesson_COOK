

from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/', PostListView.as_view(), name='post_list'),
]