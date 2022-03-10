from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Genre
from .forms import BookForm


# Create your views here.
def home (request):
    if request.user.is_authenticated:
        return redirect('list_book')
    return render (request, 'home.html')

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm()
    return render(request, "book_detail.html", {"book": book, "form": form})

def list_book(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    return render(request, "list_book.html", {"books": books, "genres": genres})

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
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
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

def title(request):
    title = Book.objects.order_by('title')
    context = {'books': title}
    return render (request, 'list_book.html', context)

def oldest(request):
    oldest = Book.objects.order_by('oldest')
    context = {'books': oldest}
    return render (request, 'list_book.html', context)

def newest(request):
    newest = Book.objects.order_by('newest')
    context = {'books': newest}
    return render (request, 'list_book.html', context)

def genre(request, slug):
    genre = get_object_or_404(genre, slug=slug)
    books = genre.books.all()

    return render(request, 'genre.html', {"genre": genre, "books": books})