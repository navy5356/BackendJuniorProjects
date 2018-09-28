from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

url(r'^(?P<bankaccount_id>[0-100]+)/$', views.detail, name='detail' ),
url(r'^(?P<Bankaccount_balance>[100-999999999])/$', views.calc, name='calc' ),

]
