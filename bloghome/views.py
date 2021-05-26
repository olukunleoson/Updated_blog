from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from bloghome.forms import CommentForm, Registration_form

def home(request):
    return render(request, 'home.html')

def post(request):
     return render(request, 'post.html')

def register(request):
    if request.method == "POST":
        form = Registration_form(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = Registration_form()
    return render(request, 'register.html', {"form": form})

def login(request, user):
    return render(request, 'post.html')

def add_comment(request, pk):
    comment = get_object_or_404(post, pk=pk)
    if request.method == "Post":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.refresh_from_db()
            comment = authenticate(username=comment.username)
            return redirect('post', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post.html', {'form': form})

def password_change(request):
    print('password change successful')
    return render(request, 'home.html')

