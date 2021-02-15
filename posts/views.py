from django.shortcuts import render, get_object_or_404
from .models import Post, Group



def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    print(slug)
    return render(request, "group.html", {"group": group, "posts": posts})

def new_post(request):
    return render(request, "new_post.html")




def details(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})


def article(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})
# # одна строка вместо тысячи слов на SQL
#     latest = Post.objects.order_by('-pub_date')[:10]
#     # собираем тексты постов в один, разделяя новой строкой
#     output = []
#     for item in latest:
#         output.append(item.text)
#     return HttpResponse('\n'.join(output))

