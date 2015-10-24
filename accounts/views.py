from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .forms import LoginForm, ChangepwdForm


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('accounts/login.html', RequestContext(request, {'form': form}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('practice/index.html', RequestContext(request))
            else:
                return render_to_response('accounts/login.html',
                                          RequestContext(request, {'form': form, 'password_is_wrong': True}))
        else:
            return render_to_response('accounts/login.html', RequestContext(request, {'form': form, }))


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('accounts.views.login'))


@login_required
def changepwd(request):
    if request.method == 'GET':
        form = ChangepwdForm()
        return render_to_response('accounts/changepwd.html', RequestContext(request, {'form': form, }))
    else:
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                return render_to_response('practice/index.html', RequestContext(request, {'changepwd_success': True}))
            else:
                return render_to_response('accounts/changepwd.html',
                                          RequestContext(request, {'form': form, 'oldpassword_is_wrong': True}))
        else:
            return render_to_response('accounts/changepwd.html', RequestContext(request, {'form': form, }))