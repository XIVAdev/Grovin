from django.contrib import admin
from django.urls import path,include
from team.views import home
from django.conf import settings
from django.conf.urls.static import static
from API.views import PortfolioViewSet,TeamViewSet
from rest_framework import routers


router=routers.SimpleRouter()
router.register('portfolioset',PortfolioViewSet)
router.register('teamset',TeamViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('api/', include(router.urls))
 
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)