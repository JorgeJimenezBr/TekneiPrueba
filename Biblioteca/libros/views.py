from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from libros.models import Category, Book
from django.contrib import messages

import json

# Create your views here.
def list_categories(request):

    categories = Category.objects.all()
    print(categories)

    return render(request, 'categories/list.html', {
        'title': 'Categorías',
        'categories': categories
    })

def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    print(category)
    return render(request, 'categories/addEdition.html', {
        'category': category,
        'title': 'Categoría',
        'button': 'Editar',
        'edition': category_id,
        'show_edition': 'd-none'
    })

def create_category(request):

    return render(request, 'categories/addEdition.html', {
        'title': 'Creación de la categoría',
        'button': 'Agregar',
        'edition': 0
    })

def save_category(request):

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        action = "creada"
        
        if request.POST['edition'] != '0':
            category = Category.objects.get(pk=request.POST['edition'])
            category.name = name
            category.description = description
            action = "editado"
        else:
            category = Category(
                name= name,
                description= description
            )

    category.save()
    messages.success(request, f"Categoría {action}: {category.name}")

    return redirect('list_categories')

def dele_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()

    return redirect('list_categories')

def list_books(request):

    books = Book.objects.all()

    return render(request, 'books/list.html', {
        'title': 'Libros',
        'books': books
    })

def book(request, book_id):

    book = get_object_or_404(Book, id=book_id)
    categories = Category.objects.all

    return render(request, 'books/addEdition.html', {
        'book': book,
        'categories': categories,
        'title': 'Libro',
        'button': 'Editar',
        'edition': book_id,
        'show_edition': 'd-none',
        'required': ''
    })

def create_book(request):

    categories = Category.objects.all

    return render(request, 'books/addEdition.html', {
        'title': 'Creación de libros',
        'categories': categories,
        'button': 'Agregar',
        'edition': 0,
        'required': 'required'
    })

def save_book(request):

    if request.method == 'POST':
        print(request.POST)
        title = request.POST['title']
        description = request.POST['description']
        author = request.POST['author']
        year = request.POST['year']
        front = request.FILES['front'] if 'front' in request.FILES else False
        categories = request.POST.getlist('categories[]')
        print(categories)
        action = "creado"
        
        if request.POST['edition'] != '0':
            book = get_object_or_404(Book, id=request.POST['edition'])
            print(book)
            book.title = title
            book.description = description
            book.author = author
            book.year = year
            if front != False:
                book.front = front
            action = "editado"

        else:
            book = Book(
                title = title,
                description = description,
                author = author,
                year = year,
                front = front,
            )

        book.save()

        if request.POST['edition'] != '0':
            book.categories.clear()

        for category in categories:
            print(category)
            book.categories.add(category)

        messages.success(request, f"Libro {action}: Título: {book.title} - Autor: {book.author}")

    return redirect('list_books')

def dele_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()

    return redirect('list_books')