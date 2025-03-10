from django.http import HttpRequest
from django.shortcuts import render
from .models import Product,Category
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# create home page
class AllProductsView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"
    def get(self, request: HttpRequest, *args, **kwargs):
        print(f"User: {request.user}")  
        # print(f"User State: {request.user._state}")  
        print(f"User ID: {request.user.id}")  
        # print(f"Last Login: {request.user.last_login}")  
        print(f"Is Superuser: {request.user.is_superuser}")  
        print(f"Username: {request.user.username}")  
        print(f"Is Authenticated: {request.user.is_authenticated}")  
        print(f"Is Anonymous: {request.user.is_anonymous}")  
        print(f"Groups: {list(request.user.groups.all())}")  


        # print(request.user.__dir__())
        return super().get(request, *args, **kwargs)


class ProductDetailsView(DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "product"
    pk_url_kwarg = "product_id"


class AllCategoriesView(ListView):
    model = Category
    template_name = "categories.html"
    context_object_name = "categories"


class CategoryProductsView(ListView):
    model= Product
    template_name = "category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return Product.objects.filter(category_id=category_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs["category_id"]

        category = Category.objects.get(id=category_id)
        context["category_name"] = category.name
        return context
       

class AddCategoryView(LoginRequiredMixin,CreateView):
    model = Category
    template_name = "forms/form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("categories")
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["title"] = "Add Category"
        context["submit"] = "Add New Category"

        return context


class AddProductView(LoginRequiredMixin,CreateView):
    model = Product
    template_name = "forms/form.html"
    form_class = ProductFrom
    success_url = reverse_lazy("home")
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["title"] = "Add Product"
        context["submit"] = "Add New Product"

        return context


class EditCategoryView(LoginRequiredMixin,UpdateView):
    model = Category
    template_name = "forms/form.html"
    extra_context = {
        "title" : "Edit Category",
        "submit" : "Update"
    }
    form_class = CategoryForm
    success_url = reverse_lazy("categories")
    pk_url_kwarg = "category_id"


class EditProductView(LoginRequiredMixin,UpdateView):

    model = Product
    template_name = "forms/form.html"
    extra_context = {
        "title": "Edit Product",
        "submit": "Update"
    }
    form_class = ProductFrom
    success_url = reverse_lazy("home")
    pk_url_kwarg = "product_id"

class DeleteProdcutView(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = "forms/delete_form.html"
    success_url = reverse_lazy("home")
    pk_url_kwarg = "product_id"
    extra_context = {
        "title": "Delete Product",
        "submit": "Delete",
        "back_to" : 'home'
    }



