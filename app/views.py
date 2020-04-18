from django.shortcuts import render,get_object_or_404
from datetime import timedelta
from django.utils import timezone
from .models import post

# Create your views here.
def home(request):
	p_obj = post.objects.all()
	current_date = timezone.now()
	a_week_ago = current_date - timedelta(7)
	context = {
		'posts':p_obj,
		'current_date':current_date,
		'a_week_ago':a_week_ago,
	}
	return render(request,'home.html',context)

# asp/list/ url
def asp_list(request,post_id):
	p_obj = get_object_or_404(post,id=post_id)
	context = {
		'post': p_obj,
	}
	return render(request,'asp_list.html',context)