from rest_framework import routers
from .api import UserViewSet

usersRouter = routers.DefaultRouter()

usersRouter.register('api/users', UserViewSet, 'users')

urlpatterns = usersRouter.urls