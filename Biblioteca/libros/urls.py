from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.list_categories, name="list_categories"), 
    path('categories/view-category/<int:category_id>', views.category, name="category"),
    path('categories/create-category', views.create_category, name="create-category"),
    path('categories/save-category',views.save_category, name="save-category"),
    path('categories/del-category/<int:category_id>',views.dele_category, name="del_category"),

    path('books', views.list_books, name="list_books"), 
    path('books/view-book/<int:book_id>', views.book, name="book"),
    path('books/create-book', views.create_book, name="create-book"),
    path('books/save-book',views.save_book, name="save-book"),
    path('books/del-book/<int:book_id>',views.dele_book, name="del_book")
]