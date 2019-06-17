from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from store.forms import LoginForm


class IndexView(TemplateView):
    template_name = 'index.html'


class StoreLoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        print(123456)
        return super().form_valid(form)


class StoreLogoutView(LogoutView):
    template_name = 'index.html'

