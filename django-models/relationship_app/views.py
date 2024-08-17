# relationship_app/view.py
from django.shortcuts import render
from relationship_app.models import Book


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})



from django.views.generic import DetailView
from relationship_app.models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'