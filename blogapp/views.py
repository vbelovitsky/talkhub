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
    query = request.GET.get('q')
    tags = Tag.objects.all()
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query)|
            Q(author__username__icontains=query)|
            Q(body__icontains=query)
        )

    context = {'posts': posts,
               'query': query,
               'tags': tags}
    return render(request, 'main/main_page.html', context)


def chat_page(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')

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
               'total_likes': post.total_likes(),
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
               'is_liked': is_liked,
               'total_likes': post.total_likes()}
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
                return HttpResponse('User is None')
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


@login_required
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


#@login_required()
#def comment_delete(request, id):
#    comment = get_object_or_404(Comment, id=id)
#    if request.user != comment.author:
#        raise Http404
#    comment.delete()
#
#    if request.is_ajax():
#        html = render_to_string('main/comment_section.html', context, request=request)
#        return JsonResponse({'form': html})
#
#
#@login_required()
#def reply_delete(request, id):
#    reply = get_object_or_404(Comment, id=id)
#    if request.user != reply.author:
#        raise Http404
#    reply.delete()
#
#    print('rep del')

