# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Sucessfully Created!")
		return redirect("posts:list")
	context = {
	'title': 'Create',
	'form': form,
	}
	return render(request, 'post_create.html', context)

def post_detail(request, post_id):
	instance = get_object_or_404(Post, id=post_id)
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

def post_update(request, post_id):
	instance = get_object_or_404(Post, id=post_id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		messages.success(request, "Sucessfully Edited!")
		return redirect(instance.get_absolute_url())
	context = {
	'form': form,
	'instance': instance,
	'title': 'Update'
	}
	return render(request, 'post_update.html', context)

def post_delete(request):
	context = {
	'title': 'Delete'
	}
	return render(request, 'post_delete.html', context)