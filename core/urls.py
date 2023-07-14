from django.urls import path
from . import views
from .forms import SignInForm
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns = [
                      path("", views.index, name="index"),
                      path("contact", views.contact, name="contact"),
                      path("signup", views.signup, name="signup"),
                      # path("signin", views.signin, name="signin"),
                      path("login/", auth_views.LoginView.as_view(authentication_form=SignInForm,
                                                                  template_name='core/signin.html'), name="signin"),
                      path("logout", views.user_logout, name="logout"),
                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns = [
        path("", views.index, name="index"),
        path("contact", views.contact, name="contact"),
    ]
