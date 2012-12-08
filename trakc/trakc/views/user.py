from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from trakc.models import Action

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

class UserRegisterView(View):
	
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')
									
        return render_to_response('register.html', context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')


        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        try:
            user = User.objects.get(email=email)
        except:
            try:
                user = User.objects.get(username=email)
            except:
                user = None

        if user is not None:
            return render_to_response('register.html',
                                {
                                    'error': 'Email already registered',
                                },
                                context_instance=RequestContext(request))

        user = User.objects.create_user(username=email,
                    email=email,
                    password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True
        user.save()

        action = Action()
        action.like_cost = 1
        action.share_cost = 1
        action.comment_cost = 1
        action.user_id = user.id
        action.save()

        # Login the user now
        user = authenticate(username=email, password=password)
        login(request, user)
        return redirect('/')

