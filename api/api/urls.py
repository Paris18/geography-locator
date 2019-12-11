#django/rest_framework imports.
from django.contrib import admin
from django.urls import include, path

# app Level imports.
from getltude import views as ltude_views

# third party imports.
from rest_framework.routers import SimpleRouter

# Intialize DefaultRouter.
router = SimpleRouter()

# register address app urls with router.
router.register(r'ltude', ltude_views.LtudeViewSet, base_name='ltude_views')


urlpatterns = [
    # path(r'admin/', admin.site.urls),
    path('api/v1/', include((router.urls, 'api'), namespace='v1')),
]