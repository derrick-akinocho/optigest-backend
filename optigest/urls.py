from django.contrib import admin
from django.urls import path

from apioptigest.views import StudentsAPIView, SectorAPIView, LoginPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/', StudentsAPIView.as_view(), name="Student API"),
    path('api/sector/', SectorAPIView.as_view(), name="Sector API"),
    path('api/login/', LoginPIView.as_view(), name="login"),
]
