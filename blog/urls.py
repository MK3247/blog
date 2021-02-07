from django.urls import path

from .views import Home, Detail, NewPost, Update, Delete

urlpatterns = [
    path('post/<int:pk>/delete/', Delete.as_view(), name = 'delete'),
    path('post/<int:pk>/edit/', Update.as_view(), name='update'),
    path('post/new/', NewPost.as_view(), name = 'new'),
    path('post/<int:pk>/', Detail.as_view(), name='detail'),
    path('', Home.as_view(), name = 'home'),
]
