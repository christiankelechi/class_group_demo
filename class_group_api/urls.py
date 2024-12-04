from django.contrib import admin
import django.urls
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import include
from rest_framework import permissions
from django.urls import path,re_path,include
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import path

schema_view = get_schema_view(
   openapi.Info(
      title="Class Group Api",
      default_version='v1',
      description="Class Group Api Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kezechristian@gmail.com"),
      license=openapi.License(name="Class group api licence"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('',include('core_app_root.routers')),

   
    
    


    


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)
