# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.views.generic import DetailView
import json
from datetime import date, datetime

# Create your views here.
post_saved = False 

def special_serialize(obj, (datetime, date)):
	serial = obj.isoformat()
	return serial

def post_article(request):
	if request.method == 'POST':
		title = request.POST.get('title', '')
		text = request.POST.get('text', '')
		is_activity = (request.POST.get('art_type', '') == 'activity')
		print is_activity
		post = Post(title=title, text=text, is_activity=is_activity)
		post.save()
		global post_saved
		post_saved = True
	return HttpResponseRedirect('../')

def get_articles(request):
	get_activities(request)
	print '*'*50
	get_news(request)
	articles = Post.objects.all().order_by('date_created')
	for article in articles:
		if len(article.title) > 20:
			article.title = article.title[:17] + '...'
	global post_saved
	post_saved = False
	return render(request, 'main/articles.html', {'articles' : articles})
#################################################################
# The following methods retrieve activities and news separately #
# as JSON files which can then be parsed						#
#################################################################

def get_activities(request):
	articles = Post.objects.filter(is_activity = True).order_by('date_created')
	article_dict_list = []
	for article in articles:
		model_dict = {}
		model_dict["title"] = article.title
		model_dict["text"] = article.text
		model_dict["date_created"] = str(article.date_created)
		article_dict_list.append(model_dict)
	json_format = {}
	json_format["articles"] = article_dict_list
	print json.dumps(json_format, sort_keys = True, indent = 4)
	return JsonResponse(json_format)

def get_news(request):
	articles = Post.objects.filter(is_activity = False).order_by('date_created')
	article_dict_list = []
	for article in articles:
		model_dict = {}
		model_dict["title"] = article.title
		model_dict["text"] = article.text
		model_dict["date_created"] = str(article.date_created)
		article_dict_list.append(model_dict)
	json_format = {}
	json_format["articles"] = article_dict_list
	print json.dumps(json_format, sort_keys = True, indent = 4)
	return JsonResponse(json_format)

def index(request):
	global post_saved
	return render(request, 'main/write_article.html', {'post_saved': post_saved})

class PostDetailView(DetailView):
	model = Post
	queryset = Post.objects.all()

	def get_object(self):
		object = super(PostDetailView, self).get_object()
		return object