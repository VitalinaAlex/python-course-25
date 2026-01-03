from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, beetroot! Notes app welcomes you.")
# Create your views here.
