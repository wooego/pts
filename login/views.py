from django.shortcuts import render,render_to_response
from django.template.context import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login/login.html',RequestContext(request,{'form':form}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return render_to_response('practice/index.html',RequestContext(request))
            else:
                return render_to_response('login/login.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
        else:
            return render_to_response('login/login.html',RequestContext(request,{'form':form,}))

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/login/")
