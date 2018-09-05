from django.conf.urls import url
from . import views

urlpatterns = [
    # /account/
    url(r'^$', views.home, name='home'),
    # /account/34567/
    url(r'^(?P<account_id>[0-9]+)/$', views.detail, name='detail'),

    # /taxman/
    url(r'^taxman/$', views.taxman, name='taxman'),

    # /account/deduct/
    url(r'^deduct/$', views.deduct, name='deduct'),

    # /account/createacc/
    url(r'^createacc/$', views.post, name='post'),

    # /account/editbal/
    url(r'^deposit/$', views.dep, name='dep'),

    # /account/withdraw/
    url(r'^withdraw/$', views.wdr, name='wdr'),

]