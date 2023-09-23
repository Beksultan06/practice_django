from django.shortcuts import render
from apps.posts.models import About, Services, Portfolio, Blog, Contacts
# Create your views here.
def index(request):
    about = About.objects.last()
    services = Services.objects.all()
    portfolio = Portfolio.objects.all()
    blog = Blog.objects.all()
    contacts = Contacts.objects.all()
    context = {
        'portfolio' : portfolio,
        'about' : about,
        'services' : services,
        'blog': blog,
        'contacts' : contacts,
    }
    return render(request, "index.html", context)

def image(request, id):
    portfolio = Portfolio.objects.get(id=id)
    context = {
        'portfolio' : portfolio,
    }
    return render(request, "portfolio-singl.html", context)

def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog' : blog,
    }
    return render (request, "blog-single.html", context)

