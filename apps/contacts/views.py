from django.shortcuts import render,redirect
from .models import Contacts
from apps.posts.models import About
from apps.telegram.views import get_text
from apps.posts.views import About,Services,Blog,Portfolio

# Create your views here.
def contacts(request):
    about =  About.objects.latest("id")
    contacts = Contacts.objects.latest("id")
    services = Services.objects.latest("id")
    blog = Blog.objects.latest("id")
    portfolio = Portfolio.objects.latest("id")


    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        phone = request.POST.get('phone')
        
        review = Contacts.objects.create(name = name, email = email,phone = phone, message = message)

        get_text(f""" Оставлен отзыв
Имя пользователя: {review.name}
Адрес(email): {review.email}
Номер телефона: {review.phone}
Текст: {review.message}
""")
        return redirect("index")
        
    context ={
        'about':about,
        'contacts':contacts,
        'services':services,
        'blog':blog,
        'portfolio':portfolio,
        
    }
    return render(request, 'index.html',context)