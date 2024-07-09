from django.shortcuts import render

def custom_404(request):
    return render(request, '404.html', status=404)

def about(request):
    return render(request, 'about.html')