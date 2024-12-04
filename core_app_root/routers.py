from rest_framework import routers
from core_app_root.viewsets import ClassListViewset

router=routers.SimpleRouter()
router.register(r'class-list',ClassListViewset,basename='class_list')


urlpatterns=[
    *router.urls
]
