from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api.urls import post_router

router = DefaultRouter()
router.registry.extend(post_router.registry)

urlpatterns = [
    # Path for the API
    path('', include(router.urls),)
]