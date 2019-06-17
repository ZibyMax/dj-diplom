from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class StoreLoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        user = User.objects.filter(email=request.POST['username'])
        print(user)
        return HttpResponseRedirect(reverse('index'))


class StoreLogoutView(LogoutView):
    template_name = 'index.html'

