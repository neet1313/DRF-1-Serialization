from django.contrib import admin
from django.urls import path, include
from API_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('API_app.urls'))
]
