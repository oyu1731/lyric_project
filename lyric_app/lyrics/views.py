from django.shortcuts import render

# Create your views here.
def index(request):
    """
    トップページのビュー
    """
    return render(request, 'lyrics/index.html')