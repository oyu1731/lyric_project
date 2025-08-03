from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# トップの簡単なビューを作成（とりあえず文字列返す）
def home(request):
    return HttpResponse("トップページです")

urlpatterns = [
    path('', home, name='home'),           # トップURLにアクセスしたときのビュー
    path('admin/', admin.site.urls),
    path('lyrics/', include('lyrics.urls')),
]
