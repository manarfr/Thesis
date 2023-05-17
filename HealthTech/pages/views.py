from django.shortcuts import render

# from django.http import HttpResponse
# Create your views here.
#def index(request):
    #return HttpResponse("Hello world")

#def about(request):
   #return HttpResponse("about page")

def index(request):
    return render(request, 'pages/index.html', {'name':'ahmd','age':'23'})