from django.shortcuts import render,HttpResponse,get_object_or_404,redirect

# Create your views here.
def HomePage(request):
    return render(request,"Course_app/index.html")