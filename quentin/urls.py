from django.conf.urls import url

from quentin import views


urlpatterns = [
    url(r'^receive/', views.receive, name='receive'),
]


