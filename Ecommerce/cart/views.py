from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def cart_page(request):
    return render(request,"cart.html")


class CartCreateView(LoginRequiredMixin, CreateView):
    model = Cart
    template_name = "forms/form.html"
    form_class = CartForm
    success_url = reverse_lazy("cart")
    extra_context = {
        "title":"Add to cart",
        "submit" : "Add"
    }

    def form_valid(self, form):
        form.instance.user = self.request.user

        product_id = self.kwargs.get('product_id')

        product = Product.objects.get(id=product_id)
        form.instance.product  = product

        #check if item already exist so increase its quantity 
        cart_item = Cart.objects.filter(user=self.request.user, product=product).first()

        if cart_item:
            cart_item.quantity += form.cleaned_data["quantity"]
            cart_item.save()
            return redirect(self.success_url)

        return super().form_valid(form)


class CartListView(LoginRequiredMixin,ListView):
    model = Cart
    template_name = "cart.html"
    context_object_name = "cart_items"

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartUpdateView(LoginRequiredMixin, UpdateView):
    model = Cart
    form_class = CartForm
    template_name = "forms/form.html"
    success_url = reverse_lazy("cart")  
    extra_context = {
        "title": "Update Cart Item",
        "submit": "Update"
    }


class CartDeleteView(LoginRequiredMixin, DeleteView):
    model = Cart
    template_name = "forms/delete_form.html"
    success_url = reverse_lazy("cart")  
    extra_context = {
        "title": "Delete Product",
        "submit": "Delete",
        "back_to" : "cart"
    }

    def get_context_data(self, **kwargs):
        """Pass the product ID to the template."""
        context = super().get_context_data(**kwargs)
        context["product"] = self.object.product
        return context

