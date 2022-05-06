"""simple_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store_app.views import CategoriesView, CategoryView, ProductView, AddCategoryModelFormView, UpdateCategoryView, \
    ProductsView, AddProductModelFormView, UpdateProductView, SearchCategoryProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', CategoriesView.as_view(), name="categories"),
    path('category/<str:slug>', CategoryView.as_view(), name="category"),
    path('product/<int:product_id>', ProductView.as_view(), name="product"),
    path('add_category/', AddCategoryModelFormView.as_view(), name="add-category"),
    path('edit_category/<str:slug>/', UpdateCategoryView.as_view(), name="edit-category"),
    path('products/', ProductsView.as_view(), name="products"),
    path('add_product/', AddProductModelFormView.as_view(), name="add-product"),
    path('edit_product/<int:pk>', UpdateProductView.as_view(), name="edit-product"),
    path('search/', SearchCategoryProductView.as_view(), name="search")
]
