from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Post, Category


class PostListPageView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'posts'


# def post_list(request):
#     context = {
#         'posts': Post.objects.filter(status=1).order_by('-created_on')
#     }
#     return render(request, 'index.html', context)


class PostDetailPageView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class CategoryPageView(generic.ListView):
    template_name = 'category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category).order_by('-created_on')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryPageView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context
