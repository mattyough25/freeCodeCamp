from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name':'Matt',
        'age':'25',
        'nationality':'American'
    }
    return render(request, 'index.html',context)