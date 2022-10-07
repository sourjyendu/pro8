from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':'satya'}
    return render(request,'for.html',d)