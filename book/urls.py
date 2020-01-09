from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('<int:n>/', views.index, name='index'),
        path('search/', views.search, name='search'),
        path('search/<str>/', views.search_next, name='search_next'),
        path('search/<str>/<int:n>/', views.search_next, name='search_next'),
        path('search_by_tags/<int:tag_id>/', views.search_by_tags, name='search_by_tags'),
        path('search_by_tags/<int:tag_id>/<int:n>', views.search_by_tags, name='search_by_tags'),
        path('model_book/<int:book_id>/', views.model_book, name='model_book'),
        path('model_book/<int:book_id>/<int:n>/', views.model_book, name='model_book'),
        path('model_page/<int:page_id>/', views.model_page, name='model_page'),
        path('model_page/<int:page_id>/<int:n>/', views.model_page, name='model_page'),
        path('model_page_content/<int:content_id>/', views.model_page_content,\
             name='model_page_content'),
        path('create_book', views.create_book, name='create_book'),
        path('create_page/<int:book_id>/', views.create_page, name='create_page'),
        path('create_content/<int:page_id>/', views.create_content, name='create_content')
    ]
