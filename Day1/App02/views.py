from django.shortcuts import render

# Create your views here.

def display_Library(request):
    authors = ["William Shakspeare", "J. K. Rowling", "Agatha Christie", "Naguib Mahfouz"]
    return render(request,"library.html", {"authors":authors})

def display_Author(request,author_Name):
    return render(request,"author.html",{"authorName":author_Name})

def display_Potter(request):
    return render(request, "potter.html")