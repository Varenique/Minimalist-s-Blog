from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comments, Like
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .forms import CommentForm
from django.contrib import auth
from django.core.paginator import Paginator


def index(request, number=1):
    all_posts = Post.objects.all().order_by('-pub_date')
    current_page = Paginator(all_posts, 3)
    #latest_posts_list = Post.objects.order_by('-pub_date')[:6]
    #template = loader.get_template('posts/index.html')
    likes = Like.objects.all()
    posts = current_page.page(number)
    cur_user = request.user.id
    like_exist = list()
    for post in posts:
        check = False
        for like in likes:
            if like.name_of_user_id == cur_user and like.post_number == post.id:
                like_exist.append(1)
                check = True
                break

        if check is False:
            like_exist.append(0)
    context = {
        'latest_posts_list': current_page.page(number), 'username': auth.get_user(request).username,
        'likes': like_exist, 'latest_posts_list_en': enumerate(current_page.page(number))

    }
    return render(request, 'index.html', context)


def detail(request, post_id):
    comment_form = CommentForm
    post = get_object_or_404(Post, pk=post_id)

    likes = Like.objects.all()
    cur_user = request.user.id

    like_exist = 0
    for like in likes:
        if like.name_of_user_id == cur_user and like.post_number == post.id:
                like_exist = 1
                break


    return render(request, 'detail.html', {'post': post,
                                           'comments': Comments.objects.filter(comment_post_id=post_id),
                                           'form': comment_form,
                                           'username': auth.get_user(request).username,
                                           'likes': like_exist})


def addlike(request, post_id, page_number=1):
    try:
        post = Post.objects.get(id=post_id)

        likes_in_bd = Like.objects.all()
        check = False
        for like in likes_in_bd:
            if like.name_of_user_id == request.user.id and like.post_number == post.id:
                like = Like.objects.get(post_number=post_id, name_of_user=request.user.id)
                like.delete()
                post.likes -= 1
                post.save()
                check = True
                break

        if check is False:
            post.likes += 1
            post.save()
            like = Like(name_of_user=request.user, post_number=post_id)
            like.save()
    except ObjectDoesNotExist:
        raise Http404
    if page_number == "0":
        return redirect('/posts/%s/' % post_id)

    return redirect('/page/%s/' % page_number)


def addcomment(request, post_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_post = Post.objects.get(id=post_id)
            comment.comment_author = request.user or 1
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/posts/%s/' % post_id)



