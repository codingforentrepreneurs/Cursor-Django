from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from .models import Article
from comments.models import Comment
from .forms import CommentForm

def article_list(request):
    articles = Article.objects.filter(is_published=True).order_by('-pub_date')
    context = {'articles': articles}
    return render(request, 'blog/article_list.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    comments = Comment.objects.filter(
        content_type=ContentType.objects.get_for_model(Article),
        object_id=article.id
    ).order_by('-created_at')
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.content_object = article
            new_comment.save()
            messages.success(request, 'Your comment has been added.')
            return redirect('blog:article_detail', pk=pk)
    else:
        form = CommentForm()
    
    context = {
        'article': article,
        'comments': comments,  # Add this line to include comments in the context
        'form': form,
    }
    return render(request, 'blog/article_detail.html', context)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    article_id = comment.content_object.id
    comment.delete()
    messages.success(request, 'Your comment has been deleted.')
    return redirect('blog:article_detail', pk=article_id)
