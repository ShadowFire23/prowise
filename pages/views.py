from django.shortcuts import render
from blog.models import Post

def index(request):
    one = Post.objects.filter(status=True)
    return render(request, 'pages/index.html', {'one':one})
