from django.contrib import admin
from apps.posts.models import About, Services, Portfolio, Blog, Contacts

admin.site.register(About)
admin.site.register(Services)
admin.site.register(Portfolio)
admin.site.register(Blog)
admin.site.register(Contacts)