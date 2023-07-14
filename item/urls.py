from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "item"
if settings.DEBUG:
    urlpatterns = [
                      path('', views.browse, name="items"),
                      path('create', views.create, name="create"),
                      path("<int:pk>/", views.show, name="show"),
                      path("<int:pk>/delete/", views.delete, name="delete"),
                      path("<int:pk>/edit/", views.edit, name="edit"),
                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
