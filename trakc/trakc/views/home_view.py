from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

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

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')

        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render_to_response('login.html',
                                    {
                                        'error': 'Your account is disabled',
                                    },
                                    context_instance=RequestContext(request))
        else:
            return render_to_response('login.html',
                                    {
                                        'error': 'Invalid email or password',
                                    },
                                    context_instance=RequestContext(request))

class UserLogoutView(View):

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            logout(request)

        return redirect('/')

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(UserLogoutView, self).dispatch(*args, **kwargs)
