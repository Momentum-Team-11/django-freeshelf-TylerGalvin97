from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


# Create your views here.
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm()
    return render(request, "book_detail.html", {"book": book, "form": form})

def list_book(request):
    books = Book.objects.all()
    return render(request, "list_book.html", {"books": books})

def add_book(request):
    if request.method =='GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_book')
    return render(request, "add_book.html", {"form": form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=Book)
    else:
        form = BookForm(data=request.POST, instance=Book)
        if form.is_valid():
            form.save()
            return redirect(to='list_book')
    return render(request, "edit_book.html", {"form": form, "book": book})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='list_book')

    return render(request, "delete_book.html", {"book": book})