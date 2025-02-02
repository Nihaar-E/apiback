from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message":"Welcome to FAQ's API....!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('faqs/', include('faqs_api.urls'))
]
