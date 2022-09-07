from django import urls
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
        path("cepstrum/",include([
            url(r'^$',views.HomePage.as_view(),name='home'),
            path('admin/', admin.site.urls),
            path('api-auth/', include('rest_framework.urls')),
            url(r'^accounts/',include('accounts.urls',namespace='accounts')),
            path('accounts/', include('allauth.urls')),
            path('inked-intellects/', include('inked_intellects.urls')),
            path('ckeditor/', include('ckeditor_uploader.urls')),
            url(r'^accounts/',include('django.contrib.auth.urls')), 
            url('bios/', include('bios.urls')),
            url('inplex/', include('inplex.urls')),
            url('team/', include('team.urls')),
            url('inphase/', include('inphase.urls')),
            url('inplace/', include('inplace.urls')),
            url('alumni/', include('alumni.urls')),
            url('talk/', include('talk.urls')),
            url('celebration/', include('celebration.urls')),
            url('paperman/', include('paperman.urls')),
            url('timetable/', include('timetable.urls')),
            url('donation/',include('donation.urls')),
            url('shop/', include('shop.urls')),
            url(r'^test/',views.TestPage.as_view(),name='test'),
            url(r'^thanks/',views.ThanksPage.as_view(),name='thanks')
    ]))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
