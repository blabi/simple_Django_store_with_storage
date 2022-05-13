from django.contrib import admin
from django.urls import path
from store_app.views import CategoriesView, CategoryView, HomeView, ProductView, AddCategoryModelFormView, UpdateCategoryView, \
    ProductsView, AddProductModelFormView, UpdateProductView, SearchCategoryProductView, HomeView

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
    path('search/', SearchCategoryProductView.as_view(), name="search"),
    path('', HomeView.as_view(), name='home'),
]
