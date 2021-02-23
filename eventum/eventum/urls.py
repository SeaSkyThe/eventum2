"""eventum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path

#Customizing fields from Admin page
admin.site.site_header = 'Administração do Eventum'
admin.site.site_title = 'Administração Eventum'
admin.site.site_url = 'http://eventum.com.br/' #change later
admin.site.index_title = 'Administração Eventum'
admin.empty_value_display = '**Vazio**'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")), #paginas de autenticacao
    url(r'^events/', include('event.urls')),
    path('', include('main.urls')), #pagina inicial, exibindo os eventos
    path('', include('subscription.urls')), #login e signin
]
