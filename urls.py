from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('backend.items.urls')),  # ✅ FIXED path
]
