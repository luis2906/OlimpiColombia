from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'OlimpiColombiaSite'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^atletas/(?P<atleta_id>[0-9]+)/$', views.AtletasView.as_view(), name='atleta'),
    url(r'^highlights/(?P<pk>[0-9]+)/$', login_required(views.HighlightView.as_view()), name='highlights'),
    url(r'^calendario/(?P<pk>\d+)/$', login_required(views.CalendarioView.as_view())),
    url(r'^accounts/login/', login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/', logout_then_login,  name='logout'),
]
