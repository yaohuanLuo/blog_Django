from django.shortcuts import render


def add_album(request):
    if request.method == 'GET':
        return render(request, 'add-notice.html')
