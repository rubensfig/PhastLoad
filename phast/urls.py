from django.conf.urls import url

from phast.views import index, submit

urlpatterns = [
    url(r'^$', index, name='main'),
    url(r'^$', submit, name='main'),

]
