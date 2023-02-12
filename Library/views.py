from django.shortcuts import render, redirect
from .models import Book
from datetime import datetime
from .forms import BookForm
# Create your views here.
def books(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect("books")
    queryset = Book.objects.filter(user=request.user).all()
    context = {"books": queryset, "date": datetime.now().date(), "form": BookForm,}
    return render(request, "books.html", context=context)