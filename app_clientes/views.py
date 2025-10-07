from django.shortcuts import render

# Create your views here.
#añadido 
def index(request):
    return render(request, 'index.html')
