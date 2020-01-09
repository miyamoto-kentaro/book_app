from django.contrib import admin
from .models import Book
from .models import Page
from .models import Page_content

admin.site.register(Book)
admin.site.register(Page)
admin.site.register(Page_content)
