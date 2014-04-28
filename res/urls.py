from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'res1.views.home', name='home'),
    url(r'^registration/$', 'res1.views.registration', name='registration'),
    url(r'^addmore/$', 'res1.views.addmore', name='addmore'),
    url(r'^profn/$', 'res1.views.profn', name='profn'),
    url(r'^email/$', 'res1.views.email', name='email'),
    url(r'^send/$', 'res1.views.send', name='send'),
    #url(r'^mail/$','res1.views.mail', name='mail'),
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

#from django.conf.urls import patterns, include, url
#from django.conf import settings
#from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

#urlpatterns = patterns('',
    
#    url(r'^$','res1.views.home'),
#    url(r'^edn/$', 'res1.views.edn'),
#    url(r'^profn/$','res1.views.profn'),
# Uncomment the admin/doc line below to enable admin documentation:
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#    url(r'^admin/', include(admin.site.urls)),
    
#)
