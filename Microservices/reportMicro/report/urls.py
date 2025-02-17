from rest_framework import routers
from .api import ReportViewSet

reportRouter = routers.DefaultRouter()

reportRouter.register('api/report', ReportViewSet, 'report')

urlpatterns = reportRouter.urls