from django.shortcuts import render
from apps.posts.models import About, Services, Portfolio, Blog, Contacts
from apps.telegram.views import get_text
# Create your views here.
def index(request):
    about = About.objects.latest('id')
    services = Services.objects.all()
    portfolio = Portfolio.objects.all()
    blog = Blog.objects.all()
    contacts = Contacts.objects.all()
    name, email, message, phone = "", "", "", ""  # Задаем значения по умолчанию

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        Contacts.objects.create(name=name, email=email, message=message, phone=phone)
        get_text(f""" Оставлен отзыв 
        Имя пользователя: {name}
        Адрес(email): {email}
        номер телефона: {phone}
        Текст: {message}
        """)

    context = {
        'portfolio': portfolio,
        'about': about,
        'services': services,
        'blog': blog,
        'contacts': contacts,
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

