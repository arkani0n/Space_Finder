from django.shortcuts import render


def history_page(request):
    return render(request, 'history/history_page.html')
