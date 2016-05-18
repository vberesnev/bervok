from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib import auth
# Create your views here.

################################ НОВОСТИ #########################################

# Список всех новостей
def news_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news/news_list.html', {'posts': posts, 'username': auth.get_user(request).username})

# Новость подробно
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    return render(request, 'news/post_detail.html', {'post': post, 'form': form, 'username': auth.get_user(request).username})

# Создание новой новости
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'news/post_edit.html', {'form': form})

# изменение новости
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('news.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'news/post_edit.html', {'form': form})    

# Удаление новости
def post_dlt(request, pk):
    post = get_object_or_404(Post, pk=pk).delete()
    return redirect('news.views.news_list')

############################# КОММЕНТАРИИ ########################################

# Дабавление нового комментария
def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    comment = form.save(commit=False)
    comment.post = post
    comment.published_date = timezone.now()
    comment.save()
    return redirect('news.views.post_detail', pk=pk)

# Удаление комментария
def comment_dlt(request, pk, id):
    comment = get_object_or_404(Comment, pk=id).delete()
    return redirect('news.views.post_detail', pk=pk)

    
    
        
          