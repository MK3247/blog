from django.views.generic import ListView, DetailView

from .models import Post

class Home(ListView):

    model = Post

    template_name = 'home.html'

    context_object_name = "all_blog_posts"

class Detail(DetailView):

    model = Post

    template_name = 'post.html'
    
