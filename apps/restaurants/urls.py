from django.conf.urls import patterns, include, url
from .views import IndexView

urlpatterns = patterns('',
	#url de inicio, incluyendo una vista basada en clases
    url(r'^$', IndexView.as_view()),

)
