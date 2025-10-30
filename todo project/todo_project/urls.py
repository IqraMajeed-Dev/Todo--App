# # todo_project/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('tasks.urls')),  # Include tasks app URLs
# ]
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Optional: Home page or root response
def home(request):
    return HttpResponse("Welcome to the meal app API! Please visit /api/ to access the endpoints.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('meals.urls')),  # API URLs
    path('', home, name='home'),  # Root URL to display a simple home page or message
]
