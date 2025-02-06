from django.shortcuts import render

# Create your views here.
def genre_homepage(request):
    return render(request,'GenreApp/genre.html')