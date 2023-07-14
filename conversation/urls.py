from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "conversation"
if settings.DEBUG:
    urlpatterns = [
                      path('', views.inbox, name="inbox"),
                      path('<int:pk>', views.show, name="conv"),
                      path('new/<int:item_pk>/', views.new_conversation, name="new"),
                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
