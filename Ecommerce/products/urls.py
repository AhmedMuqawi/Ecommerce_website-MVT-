from django.urls import path
from . import views


urlpatterns = [
    path("home/",views.AllProductsView.as_view(),name="home"),
    path("product/add/",views.AddProductView.as_view(),name="add_product"),
    path("product/edit/<int:product_id>/",views.EditProductView.as_view(),name="edit_product"),
    path("product/delete/<int:product_id>/",views.DeleteProdcutView.as_view(),name="delete_product"),
    path("product/<int:product_id>/",views.ProductDetailsView.as_view(),name="details"),
    path("category/",views.AllCategoriesView.as_view(),name="categories"),
    path("category/add/",views.AddCategoryView.as_view(),name="add_category"),
    path("category/edit/<int:category_id>/",views.EditCategoryView.as_view(),name="edit_category"),
    path("category/<int:category_id>/",views.CategoryProductsView.as_view(),name="category_products"),
    
]