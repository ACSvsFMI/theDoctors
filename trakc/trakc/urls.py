from django.conf.urls import patterns, include, url
from trakc.views import HomeView, UserLoginView, UserLogoutView, UserRegisterView
from trakc.api import trakc_api

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view()),
	url(r'^api/', include(trakc_api.urls)),
    # url(r'^trakc/', include('trakc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # Login, logout and register urls
	url(r'^login$', UserLoginView.as_view()),
	url(r'^logout$', UserLogoutView.as_view()),
	url(r'^register$', UserRegisterView.as_view()),
)

