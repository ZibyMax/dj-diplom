from itertools import count

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView

from .models import Category, Section, Product, Article


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sections'] = Section.objects.all()
        context['articles'] = Article.objects.all().prefetch_related('products')
        return context


class StoreLoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        guests = User.objects.filter(email=request.POST['username'])
        if not guests.exists():
            context['login_error'] = 'Пользователя с указанной почтой и паролем не найдено'
            return self.render_to_response(context)
        if len(guests) > 1:
            context['login_error'] = 'Обнаружено несколько пользователей с указанной почтой'
            return self.render_to_response(context)
        guest = guests.first()
        user = authenticate(request, username=guest.username, password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        context['login_error'] = 'Пользователя с указанной почтой и паролем не найдено'
        return self.render_to_response(context)


class StoreLogoutView(LogoutView):
    template_name = 'index.html'


class SectionView(ListView):
    template_name = 'section.html'

    def get_queryset(self):
        return Product.objects.filter(section=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sections'] = Section.objects.all()
        context['current_section'] = Section.objects.get(pk=self.kwargs['pk'])
        return context


class ProductView(DetailView):
    template_name = 'product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sections'] = Section.objects.all()
        return context


class CartView(ListView):
    template_name = 'cart.html'

    def get_queryset(self):
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sections'] = Section.objects.all()
        return context