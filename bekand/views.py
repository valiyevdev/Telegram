from django.shortcuts import render


def home(request):
    return render(request, 'homepage.html')


def splitter_view(request):
    context = {
        'panel1_size': 25,
        'panel2_size': 75,
        'panel1_title': 'Chap Panel',
        'panel2_title': 'Oʻng Panel'
    }
    return render(request, 'homepage.html', context)