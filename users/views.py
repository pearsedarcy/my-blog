from django.shortcuts import render, get_object_or_404
from .models import Profile
from blog.models import Post

def users_list(request):
    profiles = Profile.objects.all()
    return render(request, 'users/users_list.html', {'profiles': profiles})

def user_detail(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    posts = Post.objects.filter(author=profile.user)
    return render(request, 'users/user_detail.html', {'profile': profile, 'posts': posts})