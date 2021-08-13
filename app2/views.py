from django.shortcuts import render

# Create your views here.
def second_app(request):
    return render(request, 'second.html')