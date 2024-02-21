from django.shortcuts import render

def index(request):
    return render(request, 'Tables/index.html')
# Create your views here.
