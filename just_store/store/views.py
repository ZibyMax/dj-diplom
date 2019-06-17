from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = 'index.html'


class StoreLoginView(TemplateView):
    template_name = 'login.html'


class StoreLogoutView(LogoutView):
    template_name = 'index.html'

