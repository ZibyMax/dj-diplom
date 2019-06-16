from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class StoreLoginView(LoginView):
    template_name = 'login.html'


class StoreLogoutView(LogoutView):
    template_name = 'index.html'

