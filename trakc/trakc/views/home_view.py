from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import View

class HomeView(View):
    
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated() is False:
			return redirect('/login')

		return render_to_response('index.html', context_instance=RequestContext(request))

class UserLoginView(View):
	
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('/')
									
		return render_to_response('login.html', context_instance=RequestContext(request))

