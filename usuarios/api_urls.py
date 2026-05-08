from rest_framework.routers import DefaultRouter
from .views import PermissaoCustomViewSet

router = DefaultRouter()
router.register(r'usuarios', PermissaoCustomViewSet)

urlpatterns = router.urls