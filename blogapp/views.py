from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from blogapp.models import *
from django.db.models import Q
from .forms import *
from django.template.loader import render_to_string


def main_page(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(author__username__icontains=query) |
            Q(body__icontains=query)
        )

    tag = request.GET.get('searchtag')
    if tag:
        posts = Post.objects.filter(tag__tag_name=tag)

    qtag = request.GET.get('qtag')
    if qtag:
        tags = Tag.objects.filter(tag_name__icontains=qtag)

    context = {'posts': posts,
               'query': query,
               'tags': tags,
               'searchtag': tag}

    if request.is_ajax():
        html = render_to_string('main/tag_section.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, 'main/main_page.html', context)


def chat_page(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-timestap')

    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
            comment.save()
    else:
        comment_form = CommentForm()

    context = {'post': post,
               'is_liked': is_liked,
               'comments': comments,
               'comment_form': comment_form
               }
    if request.is_ajax():
        html = render_to_string('main/comment_section.html', context, request=request)
        return JsonResponse({'form': html})
    return render(request, 'main/chat_page.html', context)


@login_required
def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context = {'post': post,
               'is_liked': is_liked,}
    if request.is_ajax():
        html = render_to_string('main/like_section.html', context, request=request)
        return JsonResponse({'form': html})


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for item in request.POST.getlist('tags'):
                post.tag.add(item)

            return redirect('main_page')
    else:
        form = PostCreateForm()
    context = {
        'form': form,
        'tags': Tag.objects.all()
    }
    return render(request, 'main/post_create.html', context)


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('main_page'))
                else:
                    return HttpResponse('User is not active')
            else:
                context = {
                    'form': form,
                    'error': 'User with this login is not exist, or password is incorrect.'
                }
                return render(request, 'main/login.html', context)
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'main/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('main_page')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('main_page')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_form = UserEditForm(request.POST or None, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('main_page')
    else:
        edit_form = UserEditForm(instance=request.user)
    context = {
        'form': edit_form
    }
    return render(request, 'main/edit_profile.html', context)


@login_required()
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        raise Http404()
    if request.method == 'POST':
        form = PostEditForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostEditForm(instance=post)
    context = {'form': form,
               'post': post}
    return render(request, 'main/post_edit.html', context)


@login_required()
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        raise Http404
    post.delete()
    return redirect('main_page')


@login_required()
def comment_delete(request, id, comid):
    comment = get_object_or_404(Comment, id=comid)
    if request.user != comment.user and not request.user.is_staff:
        raise Http404

    comment.delete()
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post).order_by('-timestap')
    comment_form = CommentForm()

    context = {'post': post,
               'comments': comments,
               'comment_form': comment_form
               }

    if request.is_ajax():
        html = render_to_string('main/comment_section.html', context, request=request)
        return JsonResponse({'form': html})


def comment_refresh(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-timestap')
    comment_form = CommentForm()

    context = {'post': post,
               'comments': comments,
               'comment_form': comment_form
               }

    if request.is_ajax():
        html = render_to_string('main/comment_section.html', context, request=request)
        return JsonResponse({'form': html})
