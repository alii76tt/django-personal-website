from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import CategoryForm, ComentForm, PostForm, TagForm
from django.contrib import messages
from home.models import Home
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


# Create your views here.

def post_index(request):
    post_list = Post.objects.all()

    paginator = Paginator(post_list, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    query = request.GET.get('q')
    if query:
        posts = post_list.filter(
            Q(title__icontains=query) | Q(content__icontains=query)).distinct()

    context = {
        'posts': posts,
        'post_list': post_list,
        'content': Home.objects.filter(status="True"),
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    form = ComentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            comment = form.save()
            comment.post = post
            comment.ip = request.META.get('REMOTE_ADDR')
            url = request.META.get('HTTP_REFERER')
            comment.save()
            messages.success(request, 'Comment Added.')
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, 'Comment not Added.')

    context = {
        'post': post,
        'categories': categories,
        'tags': tags,
        'form': form,
        'last_posts': Post.objects.order_by('-publishing_date')[:3],
        'content': Home.objects.filter(status="True"),
    }
    return render(request, 'blog/detail.html', context)


@login_required()
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Post Created.')

            return HttpResponseRedirect(post.get_absoulte_url())

        else:
            messages.warning(request, 'Post not Created.')

    context = {
        'form': form,
        'content': Home.objects.filter(status="True"),
    }
    return render(request, 'blog/post/post_create.html', context)


@login_required()
def post_update(request, id, slug):
    post = get_object_or_404(Post, slug=slug, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Updated.')
            return HttpResponseRedirect(post.get_absoulte_url())
        else:
            messages.warning(request, 'Post not Updated.')

    context = {
        'form': form,
        'content': Home.objects.filter(status="True"),
    }
    return render(request, 'blog/post/post_update.html', context)


@login_required()
def post_delete(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    try:
        post.delete()
        messages.success(request, "Post deleted")
    except:
        messages.error(request, "Post not deleted")

    return redirect('post:index')


def category_list(request):
    context = {
        'categories': Category.objects.all(),
        'content': Home.objects.filter(status="True"),
    }
    return render(request, 'blog/category/category_list.html', context)


def category(request, slug, id):
    context = {
        'posts': Post.objects.filter(category_id=id),
        'category': Category.objects.get(id=id, slug=slug),
        'content': Home.objects.filter(status="True"),

    }
    return render(request, 'blog/category/category_index.html', context)


@login_required()
def add_category(request):
    form = CategoryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Created.')

            return redirect('post:create')

        else:
            messages.warning(request, 'Category not Created.')

    context = {
        'form': form,
        'content': Home.objects.filter(status="True"),
    }
    return render(request, 'blog/category/add_category.html', context)


@login_required()
def update_category(request, id, slug):
    category = get_object_or_404(Category, slug=slug, id=id)
    form = CategoryForm(request.POST or None, instance=category)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Updated.')
            return redirect('post:category_list')
        else:
            messages.warning(request, 'Category not Updated.')

    context = {
        'form': form,
        'content': Home.objects.filter(status="True"),
    }
    return render(request, 'blog/category/update_category.html', context)


@login_required()
def delete_category(request, id, slug):
    category = get_object_or_404(Category, id=id, slug=slug)
    try:
        category.delete()
        messages.success(request, "Category deleted")
    except:
        messages.error(request, "Category not deleted")

    return redirect('post:category_list')


def tag_list(request):
    context = {
        'tags': Tag.objects.all(),
        'content': Home.objects.filter(status="True"),
    }
    return render(request, 'blog/tag/tag_list.html', context)


def tag(request, slug, id):
    tag = get_object_or_404(Tag, slug=slug)
    context = {
        'posts': Post.objects.filter(tags=tag),
        'tag': Tag.objects.get(id=id, slug=slug),
        'content': Home.objects.filter(status="True"),

    }
    return render(request, 'blog/tag/tag_index.html', context)


@login_required()
def add_tag(request):
    form = TagForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Tag Created.')

            return redirect('post:create')

        else:
            messages.warning(request, 'Tag not Created.')

    context = {
        'form': form,
        'content': Home.objects.filter(status="True"),
    }
    return render(request, 'blog/tag/add_tag.html', context)


@login_required()
def update_tag(request, slug, id):
    tag = get_object_or_404(Tag, slug=slug, id=id)
    form = TagForm(request.POST or None, instance=tag)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Tag Updated.')

            return redirect('post:tag_list')

        else:
            messages.warning(request, 'Tag not Updated.')

    context = {
        'form': form,
        'content': Home.objects.filter(status="True"),
    }
    return render(request, 'blog/tag/update_tag.html', context)


@login_required()
def delete_tag(request, id, slug):
    tag = get_object_or_404(Tag, id=id, slug=slug)
    try:
        tag.delete()
        messages.success(request, "Tag deleted")
    except:
        messages.error(request, "Tag not deleted")

    return redirect('post:tag_list')
