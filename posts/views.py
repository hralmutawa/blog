# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_create(request):
	context = {
	'title': 'Create'
	}
	return render(request, 'post_create.html', context)

def post_detail(request):
	instance = get_object_or_404(Post, id=1000)
	context = {
	'title': 'Detail',
	'instance': instance
	}
	return render(request, 'post_detail.html', context)

def post_list(request):
	object_list = Post.objects.all()
	context = {
	'title': 'List',
	'user': request.user,
	'object_list': object_list
	}	
	return render(request, 'post_list.html', context)

def post_update(request):
	context = {
	'title': 'Update'
	}
	return render(request, 'post_update.html', context)

def post_delete(request):
	context = {
	'title': 'Delete'
	}
	return render(request, 'post_delete.html', context)