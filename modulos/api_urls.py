from rest_framework.routers import DefaultRouter
from .views import ModuloViewSet

router = DefaultRouter()
router.register(r'modulos', ModuloViewSet)

urlpatterns = router.urls