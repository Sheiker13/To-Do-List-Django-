from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="To-Do List API",
        default_version="v1",
        description="Документация для API To-Do List",
    ),
    public=True,
)

# Главная страница
from django.http import HttpResponse
def home(request):
    return HttpResponse("""
        <h1>Добро пожаловать в To-Do List API!</h1>
        <p>Доступные маршруты:</p>
        <ul>
            <li><a href='/admin/'>Админка</a></li>
            <li><a href='/todolist/'>API (Tasks, Tags, Comments)</a></li>
            <li><a href='/swagger/'>Документация Swagger</a></li>
        </ul>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', include('todolist.urls')),  # API маршруты

    # JWT-аутентификация
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Добавили этот маршрут

    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('', home),  # Корневая страница
]
