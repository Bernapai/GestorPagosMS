from rest_framework import routers
from .api import NotificacionViewSet

notificacionRouter = routers.DefaultRouter()

notificacionRouter.register('api/notificacion', NotificacionViewSet, 'notificacion')

urlpatterns = notificacionRouter.urls