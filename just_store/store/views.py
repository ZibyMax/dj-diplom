from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView

from .models import Category, Section, Product, Article


def add_to_cart(request):
    if 'add_to_cart' in request.POST:
        # if 'just_store_cart' not in request.session:
        #     request.session['just_store_cart'] = {}
        request.session.setdefault('just_store_cart', {})
        product_id = request.POST['add_to_cart']
        if product_id in request.session['just_store_cart']:
            request.session['just_store_cart'][product_id] = request.session['just_store_cart'][product_id] + 1
        else:
            request.session['just_store_cart'][product_id] = 1
        request.session.modified = True
        print(request.session['just_store_cart'])


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sections'] = Section.objects.all()
        context['articles'] = Article.objects.all().prefetch_related('products')
        if 'just_store_cart' in self.request.session:
            context['items_in_cart'] = sum(self.request.session['just_store_cart'].values())
        return context

    def post(self, request, *args, **kwargs):
        add_to_cart(request)
        return super().get(self, request, *args, **kwargs)


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sections'] = Section.objects.all()
        context['articles'] = Article.objects.all().prefetch_related('products')
        if 'just_store_cart' in self.request.session:
            context['items_in_cart'] = sum(self.request.session['just_store_cart'].values())
        return context


class SectionView(ListView):
    template_name = 'section.html'
    model = Product

    def get_queryset(self):
        return Product.objects.filter(section=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sections'] = Section.objects.all()
        context['current_section'] = Section.objects.get(pk=self.kwargs['pk'])
        if 'just_store_cart' in self.request.session:
            context['items_in_cart'] = sum(self.request.session['just_store_cart'].values())
        return context

    def post(self, request, *args, **kwargs):
        add_to_cart(request)
        return super().get(self, request, *args, **kwargs)


class ProductView(DetailView):
    template_name = 'product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sections'] = Section.objects.all()
        if 'just_store_cart' in self.request.session:
            context['items_in_cart'] = sum(self.request.session['just_store_cart'].values())
        return context

    def post(self, request, *args, **kwargs):
        add_to_cart(request)
        return super().get(self, request, *args, **kwargs)


class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sections'] = Section.objects.all()
        if 'just_store_cart' in self.request.session:
            context['items_in_cart'] = sum(self.request.session['just_store_cart'].values())
        return context

