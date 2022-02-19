"""KYS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from payment.views import homepage,paymenthandler

urlpatterns = [
    url(r'^$',views.HomePage.as_view(),name='home'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    path('accounts/', include('allauth.urls')),
    path('inked-intellects/', include('inked_intellects.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url('bios/', include('bios.urls')),
    url('team/', include('team.urls')),
    url('inphase/', include('inphase.urls')),
    url('inplace/', include('inplace.urls')),
    url('alumni/', include('alumni.urls')),
    url('celebration/', include('celebration.urls')),
    url('paperman/', include('paperman.urls')),
    url('timetable/', include('timetable.urls')),
    url('donation/',include('donation.urls')),
    path('payment/', homepage, name = 'payment'),
    path('paymenthandler/', paymenthandler, name = 'paymenthandler'),
    url('shop/', include('shop.urls')),
    url(r'^test/',views.TestPage.as_view(),name='test'),
    url(r'^thanks/',views.ThanksPage.as_view(),name='thanks'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
