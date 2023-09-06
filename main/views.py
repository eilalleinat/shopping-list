from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Taniella',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)