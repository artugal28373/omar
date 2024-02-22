from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
@api_view(["GET"])
def omar(request):
    return render(request, 'omarView.html')
