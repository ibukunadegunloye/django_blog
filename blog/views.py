from django.shortcuts import render


# Create your views here.

posts = [
    {
        'author': 'Ibukun',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted': 'November 16, 2022'
    },
    {
        'author': 'Yinka',
        'title': 'Blog Post 2',
        'content':'Second post content',
        'date_posted': 'November 17, 2022'
    },
    {
        'author': 'Goke',
        'title': 'Blog Post 3',
        'content':'Third post content',
        'date_posted': 'November 18, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return(render(request, 'blog/home.html', context))


def about(request):
    return(render(request, 'blog/about.html', {'title': 'About'}))