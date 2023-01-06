from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import path, include
from . import views

from . import views

from .views import getSentiment

from . import views

app_name = 'myproject'

urlpatterns = [

   path('', views.index, name='index'),
    url(r'^index/getSentiment$', views.getSentiment),
    url(r'^results/results$', views.results),
    url(r'^home/code$', views.code),
    #url(r'^stat/getaspect1$', views.getaspect1),
    # path('getSentiment',views.getSentiment,name='getSentiment')
    # url(r'^index/getSentiment$', views.getSentiment),
    # url(r'^insert/getaspect$', views.getaspect),
    # url(r'^fig/opinion$', views.opinion),
    # path('', views.search1, name="home"),
    # url(r'^aspect/res$', views.res),
    # path('results', views.results, name='results'),
]
