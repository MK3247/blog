from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post

from django.urls import reverse_lazy

class Home(ListView):

    model = Post

    template_name = 'home.html'

    context_object_name = "all_blog_posts"

class Detail(DetailView):

    model = Post

    template_name = 'post.html'
    
class NewPost(CreateView):

    model = Post

    template_name = 'new_post.html'

    fields = '__all__'

class Update(UpdateView):

    model = Post

    template_name = 'edit.html'

    fields = ['title', 'text']

class Delete(DeleteView):

    model = Post

    template_name = 'delete.html'

    success_url = reverse_lazy('home')