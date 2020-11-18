from django.shortcuts import render,redirect
from blog.models import Post
from .forms import SupportForm,ContactForm

def index(request):
    one = Post.objects.filter(status=True)
    return render(request, 'pages/index.html', {'one':one})

def support_create(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('support')
    else:
        form = SupportForm()
    return render(request, 'pages/support_form.html',{'form':form})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'pages/contact_form.html',{'form':form})

def new_list(request):
    news = Post.objects.filter(news=True)
    return render(request, 'pages/news.html',{'news':news})
