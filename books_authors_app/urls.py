from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('new_book', views.new_book),
    path('authors',views.authors),
    path('new_author', views.new_author),
    path('books/<int:book_id>',views.about_book),
    path('authors/<int:author_id>', views.about_author),
    path('books/add_author', views.add_author),
    path('authors/add_book', views.add_book)
]