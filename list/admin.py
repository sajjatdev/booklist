from django.contrib import admin
from list.models import Book_category, authers, bookList, Home_Slider
# Register your models here.
admin.site.register(Book_category)
admin.site.register(authers)
admin.site.register(bookList)
admin.site.register(Home_Slider)

# Admin Content Secation
admin.site.site_header = 'Online Book Shop'
admin.site.site_title = "Book shop"
admin.site.index_title = "Welcome to online Book Shop"
