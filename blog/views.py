from django.shortcuts import render, get_object_or_404 , redirect
from .models import Post , Comment
from .forms import CommentForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, url_sistem):
    posts = get_object_or_404(Post, url_sistem=url_sistem)

    comments = Comment.objects.filter(status=True,post=posts)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            kaydet = form.save(commit=False)
            kaydet.post = posts
            kaydet.save()
            return redirect('post_list')
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'posts':posts , 'comments':comments , 'form':form})
