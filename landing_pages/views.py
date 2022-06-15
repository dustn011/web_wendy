from django.shortcuts import render


def landing(request):
    return render(
        request,
        'landing_pages/landing.html'
    )

# Create your views here.
