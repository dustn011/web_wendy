# from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post
    template_name = 'wendy_store/index.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['comment_form'] = CommentForm
        return context


def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied


class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied

# def post_list(request):
#    posts = Post.objects.all().order_by('-pk')
#
#    return render(
#        request,
#        'wendy_store/post_list.html',
#        {
#            'posts': posts,
#        }
#    )

# def wendy_detail(request, pk):
#    post = Post.objects.get(pk=pk)
#
#    return render(
#        request,
#        'wendy_store/index.html',
#        {
#            'posts': post,
#        }
#    )

# Create your views here.
