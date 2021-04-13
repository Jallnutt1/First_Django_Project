from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
     all_books = Book.objects.all()
     context = {
          "books":all_books,
     }
     return render (request, "index.html", context)


def new_book(request):
     Book.objects.create(title=request.POST["title"],desc=request.POST["desc"])
     return redirect("/")


def authors(request):
     context = {
          "authors":Author.objects.all()
     }
     return render(request, "authors.html", context)


def new_author(request):
     Author.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], notes=request.POST['note'])
     return redirect('/authors')


def about_book(request, book_id):
     
     context={
          "book":Book.objects.get(id=book_id),
          "all_authors":Author.objects.all()
     }
     return render(request, "bookPage.html", context)


def about_author(request, author_id):

     context={
          "author":Author.objects.get(id=author_id),
          "all_books":Book.objects.all()
     }
     return render(request, "authorPage.html", context)

def add_author(request):
     bookNumber = request.POST['book_id']
     book_to_add_author = Book.objects.get(id = bookNumber)
     book_to_add_author.authors.add(Author.objects.get(id = request.POST['author_id']))
     return redirect(f'/books/{bookNumber}')

def add_book(request):
     authorNumber = request.POST['author_id']
     author_to_add_book = Author.objects.get(id=authorNumber)
     author_to_add_book.books.add(Book.objects.get(id = request.POST['book_id']))
     return redirect(f'/authors/{authorNumber}')