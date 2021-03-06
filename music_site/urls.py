"""music_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from users import views as users_views
from django.views.generic import TemplateView
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='users/test.html')),
    # path(r'^$', RedirectView.as_view(url='/users/', permanent=True)),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', users_views.signup, name='signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
