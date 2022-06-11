from django.shortcuts import render


def index(request):
    return render(
        request,
        'wendy_store/index.html',
    )
# Create your views here.
