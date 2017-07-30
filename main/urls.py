from django.conf.urls import url
from . import views

app_name="main"
urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^get_articles/', views.get_articles, name="get_articles"),
	url(r'^post_article/', views.post_article, name="post_article"),
	url(r'^article/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name="show_article"),
	url(r'^get_news/', views.get_news, name="get_news"),
	url(r'^get_activities/', views.get_activities, name="get_activities"),
	]